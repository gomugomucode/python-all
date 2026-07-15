# data cleaning mean fixing /remaining , incomplete incorrect data 

import pandas as pd

df = pd.read_csv('data.csv')

df.columns = df.columns.str.strip()

df.set_index('Name' , inplace = True)


# frop the irrelevent single   column  
# df = df.drop(columns = ['Legendary'])

# # to drop multiple column , we can use python list 
# df = df.drop(columns = ['Legendary','No'])

# print(df.head())


