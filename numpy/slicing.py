
import numpy as np

array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

# Slicing the array  
# Slicing syntax: array[start:stop:step]


# printing the whole array using slicing
# print(array[:])  

# print('-'*50)

# print(array[ : ])  # same as above

# print('-'*50) 

 
#  ?row slicing 

# print(array[ : : -1]) # reverse the array

# print('-'*50)

# print(array[1:3]) # prints the 2nd and 3rd rows of the array

# print(array[0:3 :1]) # prints the 1st, 2nd and 3rd rows of the array


# print(array[0:3 :2]) # prints the 1st and 3rd rows of the array

print(array[3:0:-1]) # prints the 3rd and 2nd rows of the array

