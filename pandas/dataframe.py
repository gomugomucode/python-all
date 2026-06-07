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

#  if u want to select single row from the dataframe using the integer index then we use iloc method do it like this
# print(df.iloc[0])  #iloc method is used to access the value of a
# print(df.iloc[1]) 
# print(df.iloc[2]) 
# print(df.iloc[3]) 
# print(df.iloc[4]) 



#  to add the new row in the dataframe we can do it like this


# new_row = {'Name': 'Frank', 'Age': 50}  # here we create a new row as a dictionary where the keys are the column names and the values are the data for each column.

# we cam also add the multiple rows in data frame like thsi  

new_rows = pd.DataFrame({'Name': ['Frank', 'Grace', 'Hank'], 
                          "Age": [50, 55, 60]})  # here we create a new row as a dictionary where the keys are the column names and the values are the data for each column.

# df = pd.concat([df, new_rows], ignore_index=True)  # here we use the pd.concat() function to concatenate the existing DataFrame with the new rows and the ignore_index=True argument is used to reset the index of the resulting DataFrame.


# but if u want to add the index in new row then first concat then give the index 

# 1. Combine them together
df = pd.concat([df, new_rows]) 


# 2. Overwrite the index with the complete list of 8 labels
df.index = ["a", "b", "c", "d", "e", "f", "g", "h"]   #we we dont give this then old data have index a to e and new data have index 0 to 2 which is not good so we need to give the index for new data also.

print(df)
