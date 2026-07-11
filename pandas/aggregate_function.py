
import pandas as pd

df = pd.read_csv('data.csv')

# print(df.mean())    #thisis wiull print thwe error because it select all the whole data frame and in this data frame there are some string values which cannot be converted to float so it will give error

# ?to make all the valuses i mean integer value mean we can do following

print(df.mean(numeric_only=True))  #this will print the mean of all the numeric values in the data frame and it will ignore the string values

# like above we can do other aggregate functions like sum, min, max, median, std, var, etc.
print("sum of all the numeric values in the data frame is: ", df.sum(numeric_only=True))  #this will print the sum of all the numeric values in the data frame and it will ignore the string values``

print("minimum of all the numeric values in the data frame is: ", df.min(numeric_only=True))  #this will print the minimum of all the numeric values in the data frame and it will ignore the string values

print("maximum of all the numeric values in the data frame is: ", df.max(numeric_only=True))  #this will print the maximum of all the numeric values in the data frame and it will ignore the string values

print("median of all the numeric values in the data frame is: ", df.median(numeric_only=True))  #this will print the median of all the numeric values in the data frame and it will ignore the string values


print("standard deviation of all the numeric values in the data frame is: ", df.std(numeric_only=True))  #this will print the standard deviation of all the numeric values in the data frame and it will ignore the string values

print("count of all the numeric values in the data frame is: ", df.count(numeric_only=True))  #this will print the count of all the numeric values in the data frame and it will ignore the string values
