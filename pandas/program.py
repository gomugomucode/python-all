import pandas as pd

df = pd.read_csv('data.csv' , index_col = 'Name')

pokemon  =  input("Enter the name of the pokemon : ")

try:
    print(df.loc[pokemon])
except KeyError:
    print("Pokemon not found.")