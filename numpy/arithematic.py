# scalar addition, subtraction, multiplication, and division with NumPy arrays

# Arithmetic operations in NumPy are performed element-wise, meaning that the operation is applied to each element of the array individually. This allows for efficient and concise code when performing mathematical operations on arrays.
import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# # Addition
# # in adding . it add the number to all the elements in the array and give the final result as an array

# add = arr + 5

# print("Addition:", add)

# # Subtraction
# # in subtraction . it subtract the number from all the elements in the array and give the final result as an array

# sub = arr - 10 
# print("Subtraction:", sub)

# # Multiplication
# # in multiplication . it multiply the number with all the elements in the array and give the final result as an array

# mul =  arr * 15
# print("Multiplication:", mul)

# # Division
# # in division . it divide the number with all the elements in the array and give the final result as an array

# div = arr / 20
# print("Division:", div)


# vectorize addition, subtraction, multiplication, and division with NumPy arrays

# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([10, 20, 30, 40, 50])

# # Vectorized Addition
# vec_add = arr1 + arr2
# print("Vectorized Addition:", vec_add)

# # Vectorized Subtraction
# vec_sub = arr1 - arr2   
# print("Vectorized Subtraction:", vec_sub)

# # Vectorized Multiplication
# vec_mul = arr1 * arr2   
# print("Vectorized Multiplication:", vec_mul)

# # Vectorized Division
# vec_div = arr1 / arr2
# print("Vectorized Division:", vec_div)



# vectorized mathematical functions with NumPy arrays  or vectorized mathematical operations with NumPy arrays

# arr = np.array([1, 2, 3, 4, 5])

# # Vectorized Square Root
# vec_sqrt = np.sqrt(arr)
# # print("Vectorized Square Root:", vec_sqrt)

# # Vectorized Exponential
# vec_exp = np.exp(arr)   
# print("Vectorized Exponential:", vec_exp)

# # Vectorized Logarithm
# vec_log = np.log(arr)
# print("Vectorized Logarithm:", vec_log)

# vec_log_rounded = np.round(vec_log, 2)
# print("Vectorized Logarithm (Rounded):", vec_log_rounded)

# # floor mean round down the value less than or equal to the given value and give the final result as an array
# vec_log_floored = np.floor(vec_log)
# print("Vectorized Logarithm (Floored):", vec_log_floored)

# vec_log_ceiling = np.ceil(vec_log)
# print("Vectorized Logarithm (Ceiling):", vec_log_ceiling)



# exercise

# radius  =  np.array([2,5,7,10])

# # calculate the area of the circle with the given radius and print the result as an array

# area = (np.pi * radius ** 2)
# print("Area of the circles:", area)

# # calcuate the circumference of the circle with the given radius and print the result as an array

# circum = (2 * np.pi * radius)
# print("Circumference of the circles:", circum)


# comparison operations with NumPy arrays

score = np.array([85, 90, 78, 92, 88])

# Comparison: Greater than 80
greater_than_80 = score > 80
print("Greater than 80:", greater_than_80)

# Comparison: Less than 90
less_than_90 = score < 90
print("Less than 90:", less_than_90)

# Comparison: Equal to 88
equal_to_88 = score == 88
print("Equal to 88:", equal_to_88)
