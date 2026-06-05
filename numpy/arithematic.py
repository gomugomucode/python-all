# scalar addition, subtraction, multiplication, and division with NumPy arrays

# Arithmetic operations in NumPy are performed element-wise, meaning that the operation is applied to each element of the array individually. This allows for efficient and concise code when performing mathematical operations on arrays.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Addition
# in adding . it add the number to all the elements in the array and give the final result as an array

add = arr + 5

print("Addition:", add)

# Subtraction
# in subtraction . it subtract the number from all the elements in the array and give the final result as an array

sub = arr - 10 
print("Subtraction:", sub)

# Multiplication
# in multiplication . it multiply the number with all the elements in the array and give the final result as an array

mul =  arr * 15
print("Multiplication:", mul)
