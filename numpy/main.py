import numpy as np

# # print(np.__version__)


# # passing a list in the array to create an ndarray
# # arr = np.array([1, 2, 3])

# # # passing the tuple in the array to create an ndarray
# # arr1 = np.array((1, 2, 3))

# # print("Array:", arr)
# # print("Array:", arr1)

# # print(type(arr))
# # print(type(arr1))

# # 0-d array
# # a = np.array(42)
# # print(a)

# # # 1-d array
# # arr = np.array([1, 2, 3])
# # print((arr))

# # 2-d array
# # arr = np.array([[1, 2, 3], [4, 5, 6]])

# # print(arr)

# # arr = np.array([[1,2,3,4] , [2,5,2,3] ,[1,54,6,6],[12,53,64,66]])

# # print(arr)

# # print(type(arr))
# # print(arr.ndim)

# # arr = np.array([
# #     [[1,2,3,4] ,
# #      [2,5,2,3]] 
# #     ,[[1,54,6,6],
# #     [12,53,64,66]]
# #     ])

# # print(arr)

# # print(type(arr))
# # print(arr.ndim)

# arr = np.array([1, 2, 3, 4 , 9, 0 ], ndmin=5)

# print(arr)

# # Structure (rows, cols)
# print(arr.shape)

# # total no. of elements contained in the array
# print(arr.size)

# # in reshape the first element it take is row and second is column i.e. reshape(row , column) it onnly change the structure not the data or elements
# print(arr.reshape(2 ,-1))
# print(arr.reshape(-1 ,2))
# print('number of dimensions :', arr.ndim)


arr = np.array([1, 2, 3, 4, 5, 6])
print(arr[3])
print(arr[ :3])
print(arr[ :])
print(arr[ -1:])
print(arr.ndim)
print(len(arr.shape) == arr.ndim)
