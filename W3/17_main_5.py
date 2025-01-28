import requests
from bs4 import BeautifulSoup

def display_coronavirus_data():
    url = "https://www.worldometers.info/coronavirus/"
    response = requests.get(url)

    if(response.status_code == 200):
        countries_data = dict()
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find('table', {'id': 'main_table_countries_today'})

        rows = table.find_all('tr')[1:]
        for row in rows:
            columns = row.find_all('td')
            if len(columns) < 7:
                continue

            country_name = columns[1].text.strip()
            total_cases = columns[2].text.strip()
            total_deaths = columns[4].text.strip()
            total_recovered = columns[6].text.strip()

            countries_data[country_name] = [total_cases, total_deaths, total_recovered]
        # for data in countries_data:
        #     for country, lst in data.items():
        #         print(country, ": ", lst)
        for country, data in countries_data.items():
            print(f"{country}: Cases = {data[0]}, Deaths = {data[1]}, Recovered = {data[2]}")

    else:
        print("cant fetch results from worldometer")

display_coronavirus_data()