import numpy as np

arr1 = np.array([[1,2,3,4,5,6,7,8,9],
                 [10,11,12,13,14,15,16,17,18],
                 [19,20,21,22,23,24,25,26,27]])  

print(arr1.shape)

# print(np.sum(arr1))  # this will give us the sum of all the elements in the array
# print(np.mean(arr1))  # this will give us the mean of all the elements in the array
# print(np.min(arr1))  # this will give us the minimum value in the array
# # print(np.max(arr1))  # this will give us the maximum value in the array
# print(np.average(arr1))  # this will give us the average of all the elements in the array
# print(np.var(arr1))  # this will give us the variance of all the elements in the array
# print(np.std(arr1))  # this will give us the standard deviation of all the elements in the array

# print(np.argmax(arr1))  # this will give us the index of the maximum value in the array
# print(np.argmin(arr1))  # this will give us the index of the minimum value in the array

# print(np.prod(arr1))  # this will give us the product of all the elements in the array

# print(np.cumsum(arr1))  # this will give us the cumulative sum of all the elements in the array
print(np.cumprod(arr1))  # this will give us the cumulative product of all the elements in the array
