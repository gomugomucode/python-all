
# series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index. The basic method to create a Series is to call:

import pandas as pd

# in series we can create data in the form of list and then we can use the pd.Series() function to create a series from the list. The resulting Series will have an index starting from 0 and the values will be the data from the list.

# s = pd.Series([1, 3, 5, 7, 9])
# print(s)

# we can also do this for above code snippet

# name =["Tailoring / Sewing", "Handicrafts (knitting, beadwork, etc.)", "Embroidery Work", "Hand Embroidery", "Pote/Mala Making", "Cloth Bag Making", "Paper Bag Making", "Knitting and Crocheting", "Jewelry Making", "Traditional Broom Making", "Bamboo Crafting", "Traditional Sculpture", "Pottery", "Candle Making", "Soap Making", "Agarbatti Making", "Pickle Making and Selling", "Fish Pickle Making and Selling", "Homemade Snacks and Food Delivery", "Catering Service (small scale)", "Baking and Cake Decoration", "Jam, Jelly and Sauce Production", "Nepali Food Recipe Content Creation", "Vegetable Farming", "Mushroom Farming", "Indoor Plant Selling / Kitchen Garden Setup", "Organic Compost Production", "Content Writing", "Digital Marketing", "Web Development", "Graphic Design", "Photography", "Bookkeeping / Accounting", "Data Entry Operator", "Nepali Recipe Blog / YouTube Channel", "Affiliate Marketing / Blogging", "Online Course Creation", "Virtual Assistant Services", "Makeup Artist", "Beauty Parlor Service", "Event Planning"]

# # creating a series from the list of names
# s = pd.Series(name) #  here the padnas library is used to create a series from the list of names. The pd.Series() function takes the list as an argument and returns a Series object. The resulting Series will have an index starting from 0 and the values will be the names from the list.

# print(s)

age = [25, 30, 35, 40, 45]

# series_age = pd.Series(age)

# in the above code , we can also give index to the series
series_age = pd.Series(age, index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'])

# print(series_age)

# if we want to access the value of a specific index, we can do it like this

# print(series_age['Alice'])

# or we can use loc method to access the value of a specific position
# print(series_age.loc['Alice'])  #loc method is used to access the value of a specific position using the index label of line 23 

# # if we wan to access the value of a specific index , we cna do it by using iloc method which is used to access the value of a specific position using the integer index of line 23
# print(series_age.iloc[0])  #iloc method is used to access the value of a specific position using the integer index of line 23, here it will return the value of the first position which is 25.

# print(series_age.iloc[1])
# print(series_age.iloc[2])
# print(series_age.iloc[3])
# print(series_age.iloc[4])

# loc select the data according to custom labels and iloc select the data according to the integer index.

# if we want the filter value of the series we can do it like this
print(series_age[series_age > 30])  # this will return the values of the series which are greater than 30.

print(series_age[series_age < 30])  # this will return the values of the series which are less than 30.