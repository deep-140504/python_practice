import requests
from bs4 import BeautifulSoup

def countries_with_all_corona_patient_dead():
    url = "https://www.worldometers.info/coronavirus/"
    response = requests.get(url)

    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find('table', {'id': 'main_table_countries_today'})

        countries_data = []
        rows = table.find_all('tr')[1:]

        for row in rows:
            columns = row.find_all('td')
            if(len(columns) < 8):
                continue
            country_name = columns[1].text.strip()
            try:
                total_cases = int(columns[2].text.strip().replace(',', ''))
                total_death_text = columns[4].text.strip().replace(',', '')
                if not total_death_text.isdigit():
                    continue
                total_deaths = int(total_death_text)

                if total_deaths == total_cases and total_cases > 0:
                    countries_data.append(country_name)
            except ValueError:
                continue

        if countries_data:
            for country in countries_data:
                print("Countries with equal cases and death are: ")
                print(country)
        else:
            print("There are no such countries having same deaths and cases")
    else:
        print("cant fetch results from worldometer")

countries_with_all_corona_patient_dead()