
import numpy as np

ages  =  np.array([[22, 25, 18, 30, 28, 35, 40 , 27, 24 ,65,999],[32,98 ,65 , 45, 50, 60, 70, 80, 90, 100 , 1]])

# teenagers = ages < 25 # in here the teenagers variable  if the condition matched then the matched value will be replaced by boolean value "true" and unmatched value will be replaced by boolean value "false"

# # if we want only the value tha match the condition then we can do it like this 
# teenagers = ages[ages < 25] # in here the teenagers variable will only contain the value that match the condition

# print(teenagers)

#  but in above it gives us value that math the condition in 1d array whatever the array dimension is 

# so to preserve the array dimentionwe use the where function

# teenagers = np.where(ages < 25, ages, 0) # in here the teenagers variable will contain the value  1 for  match the condition and the unmatched value will be replaced by 0 without changing the array dimension
# print(teenagers)


# adult = ages[ages >= 25]
# print(adult)

#  we can use multiple condition in where function

# people = np.where((ages >= 25 ) & (ages <60) , "Adult" , np.where(ages < 25 , "Teenager" , "Senior Citizen")) # in here the people variable will contain the value "Adult" for match the first condition and the unmatched value will be checked for the second condition if it match then it will be replaced by "Teenager" and if it does not match then it will be replaced by "Senior Citizen"

# print(people)

#  the anothe rway of doing this is by using the select function

conditions = [ (ages < 25) , (ages >= 25) & (ages < 60) , (ages >= 60)]
choices = ["Teenager" , "Adult" , "Senior Citizen"]
people = np.select(conditions , choices , default="Unknown") # in here the people variable will contain the value "Teenager" for match the first condition and the unmatched value will be checked for the second condition if it match then it will be replaced by "Adult" and if it does not match then it will be replaced by "Senior Citizen"
print(people)
