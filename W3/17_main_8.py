import requests
from bs4 import BeautifulSoup

def countries_with_complete_recovery():
    url = "https://www.worldometers.info/coronavirus/"
    response = requests.get(url)
    
    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'id': 'main_table_countries_today'})

        countries_data = []
        rows = table.find_all('tr')[1:]

        for row in rows:
            columns = row.find_all('td')
            if len(columns) < 8:
                continue
            country_name = columns[1].text.strip()

            try:
                total_cases = int(columns[2].text.strip().replace(',', ''))
                total_recovered_cases_text = columns[6].text.strip().replace(',', '')

                if total_recovered_cases_text == 'N/A' or not total_recovered_cases_text.isdigit():
                    continue
                total_recovered = int(total_recovered_cases_text)

                if total_cases == total_recovered and total_cases > 0:
                    countries_data.append(country_name)
            except ValueError:
                continue
        if countries_data:
            print("Countries with all COVID-19 cases recovered: ")
            for country in countries_data:
                print(country)
        else:
            print("No countries currently have all cases fully recovered")
    else:
        print(f"Failed to fetch data from {url}")

countries_with_complete_recovery()