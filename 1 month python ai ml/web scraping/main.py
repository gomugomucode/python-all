import pandas as pd
import requests
from bs4 import BeautifulSoup

# ==============================================================================
# Web Scraping Worldometers COVID-19 Data
# ==============================================================================

# Step 1: Define the target URL for scraping
url = "https://www.worldometers.info/coronavirus/"

# Step 2: Send an HTTP GET request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 3: Parse the raw HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Step 4: Locate the main coronavirus data table using its HTML ID
    table = soup.find("table", {"id": "main_table_countries_today"})

    header = []
    rows = []

    if table:
        # Step 5: Extract table headers (<th> tags)
        for th in table.find_all("th"):
            header.append(th.text.strip())

        # Step 6: Extract row data (<tr> and <td> tags) skipping the header row
        for tr in table.find_all("tr")[1:]:
            tds = tr.find_all("td")
            if tds:
                row_data = [td.text.strip() for td in tds]
                # Ensure row column count matches header column count
                if len(row_data) == len(header):
                    rows.append(row_data)

        # Step 7: Convert extracted data into a Pandas DataFrame
        df = pd.DataFrame(rows, columns=header)

        # Display preview of scraped dataset
        print("Data scraped successfully!")
        print(df.head())

        # Step 8: Save dataset to a CSV file
        csv_filename = "world_ometers_corona_data.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Data saved successfully to {csv_filename}")
    else:
        print("Error: Target table 'main_table_countries_today' not found on the page.")
else:
    print(f"Error: Failed to fetch webpage. HTTP Status Code: {response.status_code}")
