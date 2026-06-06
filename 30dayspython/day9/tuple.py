
# # creating tuple

# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)

# # creating a tuple with one element
# my_tuple = (1,)
# print(my_tuple)

# # creating a tuple without parentheses
# my_tuple = 1, 2, 3, 4, 5
# print(my_tuple)

# # creating a tuple from a list
# my_list = [1, 2, 3, 4, 5]
# my_tuple = tuple(my_list)
# print(my_tuple)

# # creating a tuple from a string
# my_string = "Hello"
# my_tuple = tuple(my_string)
# print(my_tuple)

# # creating a tuple from a set
# my_set = {1, 2, 3, 4, 5}
# my_tuple = tuple(my_set)
# print(my_tuple)

# # creating a tuple from a dictionary
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_tuple = tuple(my_dict)
# print(my_tuple)

# print('\n-----------------------------   \n')  

# # accessing tuple elements

# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[0])  # accessing the first element
# print(my_tuple[1])  # accessing the second element
# print(my_tuple[2])  # accessing the third element
# print(my_tuple[3])  # accessing the fourth element
# print(my_tuple[4])  # accessing the fifth element
 
# print('\n-----------------------------   \n')  

# fruit_tuple = ('apple', 'banana', 'cherry')
# print(fruit_tuple[0])  # accessing the first element
# print(fruit_tuple[1])  # accessing the second element
# print(fruit_tuple[2])  # accessing the third element

# print('\n-----------------------------   \n')  

# # accessing tuple elements using negative indexing
# print(my_tuple[-1])  # accessing the last element
# print(my_tuple[-2])  # accessing the second last element
# print(my_tuple[-3])  # accessing the third last element
# print(my_tuple[-4])  # accessing the fourth last element
# print(my_tuple[-5])  # accessing the fifth last element

# print('\n-----------------------------   \n')  

# print(fruit_tuple[-1])  # accessing the last element
# print(fruit_tuple[-2])  # accessing the second last element
# print(fruit_tuple[-3])  # accessing the third last element



print('\n-----------------------------   \n')  


# tuple packing and unpacking
# packing is the process of assigning multiple values to a single variable, while unpacking is the process of assigning the values of a tuple to multiple variables.

# packing a tuple
student = ("Anupam" ,21 ,"Python Developer")

# unpacking a tuple 

name, age, role = student

print(f" Name of the student is {name}")
print(f" Age of the student is {age}")
print(f" Role of the student is {role}")

print('\n-----------------------------   \n')  

# Extended Unpacking (Using the * Operator)

numbers = (1, 2, 3, 4, 5)

# If you do not know the tuple's exact size or only want specific items, you can prefix a variable name with an asterisk (*) to capture the remaining items as a list

# Captures the first, last, and pools everything else into 'middle'
first, *middle, last = numbers

print(first)   
print(middle)  
print(last)    
