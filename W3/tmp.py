import requests
from bs4 import BeautifulSoup

def fetch_coronavirus_data():
    url = "https://www.worldometers.info/coronavirus/"
    response = requests.get(url)

    if(response.status_code == 200):
        countries_data = []
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find('table', {'id': 'main_table_countries_today'})

        # Fetch rows in the table, excluding the header
        rows = table.find_all('tr')[1:]  # Skipping the first row (header)

        # Define a list of non-country entities to exclude (like continents, world, etc.)
        non_country_entities = ["World", "North America", "Asia", "Europe", "Africa", "Oceania", "South America"]

        for row in rows:
            columns = row.find_all('td')
            if len(columns) < 7:  # Skip rows with insufficient data
                continue

            # Extract data from each column
            country_name = columns[1].text.strip()
            
            # Skip rows that represent continents or world
            if country_name in non_country_entities:
                continue

            total_cases = columns[2].text.strip().replace(",", "")
            total_deaths = columns[4].text.strip().replace(",", "")
            total_recovered = columns[6].text.strip().replace(",", "")

            # Save the extracted data in a dictionary
            countries_data.append({
                'country': country_name,
                'total_cases': total_cases,
                'total_deaths': total_deaths,
                'total_recovered': total_recovered
            })

        # Output the extracted data
        for country_data in countries_data:
            print(f"Country: {country_data['country']}")
            print(f"Total Cases: {country_data['total_cases']}")
            print(f"Total Deaths: {country_data['total_deaths']}")
            print(f"Total Recovered: {country_data['total_recovered']}")
            print("-" * 40)
    else:
        print("Failed to fetch data from Worldometer")

# Call the function to fetch and display data
fetch_coronavirus_data()
