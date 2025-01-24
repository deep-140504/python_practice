import threading
import requests
def download_file(url, filename):
    try:
        response = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {filename} successfully")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
    
def main():
    urls = [
        ("https://example.com/file1.jpg", "file1.jpg"),
        ("https://example.com/file2.jpg", "file2.jpg"),
        ("https://example.com/file3.jpg", "file3.jpg")
    ]
    threads = []
    for url, filename in urls:
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()