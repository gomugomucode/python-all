import pandas as pd

df = pd.read_csv('data.csv')

# selection by column name
#  syntax is :   selected_column = df['column_name']

# print(df["Name"])

# to print the full dataframe without truncation
# pd.set_option('display.max_rows', None)
# print(df["Name"])


# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df["Type1"])
# print(df["Type2"])


# selecting multiple column
# for that we must pass python list

# print(df[["Name" , "Height" , "Weight"]])

# selecting by rows

# print(df.loc[0])

# we can set teh index of file  by column name while reading the file using index_col parameter
df = pd.read_csv('data.csv' , index_col = "Name")

# # print(df.loc["Bulbasaur"])
# print(df.loc["Bulbasaur" , "Height"])
# print(df.loc["Pikachu" ,["Height" , "Weight"]])

