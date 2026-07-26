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

# print(header)

row = []

for tr in table.find_all("tr")[1:]:
    td = tr.find_all("td")
    row.append([td[i].text.strip() for i in range(len(td))])

# print(row)

df = pd.DataFrame(row, columns=header)
print(df)

df.to_csv("world_ometers_corona_data.csv", index=False)
print("data saved to world_ometers_corona_data.csv")
