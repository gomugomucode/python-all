
# /html/body/div[1]/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody


import pandas as pd
import numpy as np

from selenium import webdriver  # opent he website
from selenium.webdriver.common.by import By  #element locate

# from selenium.webdriver.common.keys import Keys
# import time




driver = webdriver.Chrome() 
driver.get("https://www.iplt20.com/stats/2026")

objr = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody")

data = objr.text

# data.split()
all_data = data.split("\n")[1:]
all_data[:10]

all_data = np.array(all_data)

all_data.reshape(167, 4)
df = pd.DataFrame(all_data)

df[3][0].split(" ")
temp = df[3].str.split(expand=True)
df.drop(columns=3 , inplace=True)
df.head()
temp.drop(columns=3 , inplace=True)
pd.concat(df , temp ,axis=1)
final = df.drop(columns=3 , inplace=True)



# (len(data))
# (data[:100])
# print(objr)
# print(data)
# print(all_data)
# print(all_data.ndim)
# print(df)