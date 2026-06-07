# dataframe are teh tablur data satructure with rows and column 2D data structure. It is similar to a spreadsheet or a SQL table. It is one of the most commonly used data structures in pandas. The basic method to create a DataFrame is to call:

import pandas as pd

# in dataframe we create data in the form of dictionary where the keys are the column names and the values are the data for each column. The pd.DataFrame() function takes the dictionary as an argument and returns a DataFrame object. The resulting DataFrame will have columns named 'Name' and 'Age' with the corresponding data.

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], 'Age': [25, 30, 35, 40, 45]}

df = pd.DataFrame(data)

print(df)