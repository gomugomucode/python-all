# In this code, we are exploring slicing in NumPy arrays. Slicing allows us to extract specific parts of an array based on specified indices and steps. We will demonstrate how to slice rows, columns, and both together in a 2D array.
# Slicing syntax: array[start:stop:step]
# In slicing, the 'start' index is inclusive, while the 'stop' index is exclusive. The 'step' parameter determines the interval between indices in the slice. If 'step' is negative, it will slice in reverse order.

import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

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

# print(array[3:0:-1]) # prints the 3rd and 2nd rows of the array




# column slicing
# print(array[:, 0:3]) # prints the 1st, 2nd and 3rd columns of the array

# print(array[ : , : -1]) # prints all the column except last one 

# print(array[ : , 0:3 :2]) # prints the 1st and 3rd columns of the array

# print(array[ : , 3:0:-1]) # prints the 4th and 3rd columns of the array

# print(array[ : , -1]) # prints the last column of the array

# print(array[ : , -2]) # prints the second last column of the array

# print(array[ 1:3 , 2]) # prints the 3rd column of the 2nd and 3rd rows of the array



# row and colum slicing together

# in row and coumn slicing . it first select the rows and then select the columns from the selected rows

# print(array[0 , 0]) # prints the element at 1st row and 1st column of the array

# print(array[1,1]) # prints the element at 2nd row and 2nd column of the array

# print(array[2,2]) # prints the element at 3rd row and 3rd column of the array

# print(array[3,3]) # prints the element at 4th row and 4th column of the array

# print(array[0:3, 0:3]) # prints the 1st, 2nd and 3rd rows and columns of the array

# print(array[0:2 , 0:2]) # prints the 1st and 2nd rows and columns of the array

print(array[0:3 :2 , 0:3 :2]) # prints the 1st and 3rd rows and columns of the array