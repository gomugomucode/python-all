from urllib3 import response
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

print(soup)
