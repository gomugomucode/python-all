
# import pandas as pd

# df = pd.read_csv('data.csv')

# # print(df.mean())    #thisis wiull print thwe error because it select all the whole data frame and in this data frame there are some string values which cannot be converted to float so it will give error

# # ?to make all the valuses i mean integer value mean we can do following

# print(df.mean(numeric_only=True))  #this will print the mean of all the numeric values in the data frame and it will ignore the string values

# # like above we can do other aggregate functions like sum, min, max, median, std, var, etc.
# print("sum of all the numeric values in the data frame is: ", df.sum(numeric_only=True))  #this will print the sum of all the numeric values in the data frame and it will ignore the string values``

# print("minimum of all the numeric values in the data frame is: ", df.min(numeric_only=True))  #this will print the minimum of all the numeric values in the data frame and it will ignore the string values

# print("maximum of all the numeric values in the data frame is: ", df.max(numeric_only=True))  #this will print the maximum of all the numeric values in the data frame and it will ignore the string values

# print("median of all the numeric values in the data frame is: ", df.median(numeric_only=True))  #this will print the median of all the numeric values in the data frame and it will ignore the string values


# print("standard deviation of all the numeric values in the data frame is: ", df.std(numeric_only=True))  #this will print the standard deviation of all the numeric values in the data frame and it will ignore the string values

# print("count of all the numeric values in the data frame is: ", df.count(numeric_only=True))  #this will print the count of all the numeric values in the data frame and it will ignore the string values




# selecting the single coulum to do aggreate functions

# import pandas as pd

# # 1. Load the CSV without setting the index yet
# df = pd.read_csv('data.csv')

# # 2. Clean the column headers to remove hidden spaces
# df.columns = df.columns.str.strip()

# # 3. Set the 'Name' column as the index now that it is cleaned
# df.set_index('Name', inplace=True)

# print("Mean Height:", df['Height'].mean(numeric_only=True))

# print("Sum of Weight:", df['Weight'].sum(numeric_only=True))

# print("Minimum Height:", df['Height'].min(numeric_only=True))

# print("Maximum Weight:", df['Weight'].max(numeric_only=True))



