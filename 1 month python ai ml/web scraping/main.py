import pandas as pd
import requests
from bs4 import BeautifulSoup


url = "https://www.worldometers.info/coronavirus/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# print(soup)

table = soup.find("table", {"id": "main_table_countries_today"})

# print(table)
header = []

if table:
    for th in table.find_all("th"):
        header.append(th.text.strip())

print(header)
