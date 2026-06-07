# dataframe are teh tablur data satructure with rows and column 2D data structure. It is similar to a spreadsheet or a SQL table. It is one of the most commonly used data structures in pandas. The basic method to create a DataFrame is to call:

import pandas as pd

# in dataframe we create data in the form of dictionary where the keys are the column names and the values are the data for each column. The pd.DataFrame() function takes the dictionary as an argument and returns a DataFrame object. The resulting DataFrame will have columns named 'Name' and 'Age' with the corresponding data.

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], 'Age': [25, 30, 35, 40, 45]}

# df = pd.DataFrame(data)  #by default it has index in numeric form starting from 0. We can also give index to the dataframe like this :

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])  # here the index is given as a list of strings ['a', 'b', 'c', 'd', 'e'] which will be used as the index for the DataFrame. 

# if u need tho select single row from the dataframe using the custom index given to it then we use loc method do it like this
# print(df.loc['a'])  #loc method is used to access the value of a specific position using the index label of line 23
# print(df.loc['b'])
# print(df.loc['c'])
# print(df.loc['d'])
# print(df.loc['e'])

# print(df)