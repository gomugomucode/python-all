
import pandas as pd

#  to read a CSV file and create a DataFrame
df = pd.read_csv('data.csv')

#  we can do same for other file formats like Excel, JSON, etc.
# df = pd.read_excel('data.xlsx')
# df = pd.read_json('data.json')

# .head() method is used to display the first few rows of the DataFrame
# print(df.head())
 
# .info() method is used to get a concise summary of the DataFrame
# print(df.info())

# .describe() method is used to generate descriptive statistics of the DataFrame
# print(df.describe())

# this print the some daya from first 5 rows  and last 5 rows of the DataFrame
# print(df)

# to print the all the data without truncating
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# print(df)

# or we can do it like this also 
print(df.to_string())