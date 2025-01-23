import threading
import requests
from urllib.parse import urljoin
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import csv

#robot scarper class
class RobotParser:
    def __init__(self, base_url):
        self.base_url = base_url
        self.allowed_paths = set()
        self.diallowed_paths = set()
        self.parse_robots_txt()
    
    # parse_robots_txt function
    def parse_robots_txt(self):
        robots_url = urljoin(self.base_url, "robots.txt")
        try:
            response = requests.get(robots_url, timeout=5)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines:
                    # this checks if the line starts with "Disallow:"
                    if line.startswith("Disallow:"):
                        # "[len("Disallow:"):]" this will first do the slicing from ending index of string "Disallow" with the use of len and then will strip any leading or trailing spaces 
                        path = line[len("Disallow:"):].strip()
                        self.diallowed_paths.add(path)
                    elif line.startswith("Allow:"):
                        path = line[len("Allow:"):].strip()
                        self.allowed_paths.add(path)
            print(f"successfully fetched robots.txt from {robots_url}.")
        except requests.exceptions.RequestException:
            print(f"failed to fetch eobots.txt from {robots_url}. Assuming full access.")
    
    # determining whether the utl_path is allowed to be accessed or not
    def is_allowed(self, url_path):
        for disallowed_path in self.diallowed_paths:
            if url_path.startswith(disallowed_path):
                return False
        return True


class MultiThreadScrapper:
    # initialization of attributes
    def __init__(self, base_url, max_threads = 5):
        self.base_url = base_url
        self.visited_urls = set() # already visited url
        self.max_threads = max_threads
        self.queue = [] # url that still needs to be scrapped
        self.lock = threading.Lock() # lock for thread safety
        self.robots_parser = RobotParser(base_url) # respect Robots.txt
        self.found_urls = [] # list to store the scrapped urls
    
    # fetching a url
    def fetch_url(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
        return None
    
    # extracting links
    def parse_links(self, html):
        soup = BeautifulSoup(html, "html.parser")
        links = set()
        for a_tag in soup.find_all('a', href = True):
            full_url = urljoin(self.base_url, a_tag["href"])
            # urlparse is used to breakdown the components of full url, one of such component is netloc, which specifies the domain of the url parsed
            parsed_url = urlparse(full_url)
            # here, in this case, addition in links set is done only if the domain of base url and parsed url is same, so using this condition only internal links are added and external links are neglected
            if parsed_url.netloc == urlparse(self.base_url).netloc:
                links.add(full_url)
        return links

    # scraping a url
    def scrape_url(self, url):
        with self.lock:
            if url in self.visited_urls:
                return
            self.visited_urls.add(url) # storing visted urls
        print(f"scraping: {url}")
        self.found_urls.append(url) # storing found urls

        html = self.fetch_url(url)
        if html: # executing the block only if the html fetched is not Nont
            links =  self.parse_links(html)
            with self.lock:
                for link in links:
                    # this conditional statement determines whether, the url is present in the visited url or not and is allowed to be process upon
                    if link not in self.visited_urls and self.robots_parser.is_allowed(urlparse(link).path):
                        self.queue.append(link)
                        # appending the links that needs to be fetched inside of the queue
    
    def worker(self):
        while True:
            with self.lock:
                if not self.queue:
                    return # if the queue is empty, then loop will break
                url = self.queue.pop(0)
            self.scrape_url(url)
    
    def save_to_csv(self, filename="scraped_urls.csv"):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Scraped URLs"]) # this will be the header of the file
            for url in self.found_urls:
                writer.writerow([url]) # here url and "Scraped URLs" is wrapped inside of the list, as the writerow accepts only iterable as an argument

    def save_to_text_file(self, filename="scarped_urls.txt"):
        with open(filename, "w") as file:
            for url in self.visited_urls:
                file.write(url + "\n")


    def run(self, start_path = "/"):
        # the start_path is an optional argument, so it will append the baseurl with the start_path, in this case, the first url that will be added to the queue for the processing will be, https://quotes.toscrape.com + / = https://quotes.toscrape.com/
        self.queue.append(urljoin(self.base_url, start_path))
        threads = [] # this stores instances of all the threads being created
        for _ in range(self.max_threads):
            t = threading.Thread(target=self.worker)
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        self.save_to_csv()
        self.save_to_text_file()

if __name__ == "__main__":
    base_url = "https://quotes.toscrape.com/"
    scraper = MultiThreadScrapper(base_url, max_threads=5)
    scraper.run(start_path="/")