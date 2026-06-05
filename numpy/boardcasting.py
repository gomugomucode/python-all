
import numpy as np

# arr1 = np.array([[1,2,3,4,5]])

# arr2 = np.array([[1],[2],[3],[4],[5]])

# shape of arr1 is (1,5) and shape of arr2 is (5,1) but they can be multiplied together because of broadcasting rules in numpy. The resulting shape will be (5,5) because the first dimension of arr1 will be broadcasted to match the first dimension of arr2 and the second dimension of arr2 will be broadcasted to match the second dimension of arr1.

# in broadcasting , we can perform operation only if the dimensions of the arrays are compatible. Two dimensions are compatible when they are equal, or one of them is 1. If the dimensions are not compatible, a ValueError will be raised.

# print(arr1.shape)

# print(arr2.shape)

# mul_array = arr1 * arr2
# print(mul_array)

a1 = np.array([1 ,2])  # 1d array 1 row 2 column 
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 2d array 3 row 3 column

print(a1.shape)
print(a2.shape)

mul_array = a1 * a2
print(mul_array)  # in this part we get an error because the shape of a1 is (2,) and the shape of a2 is (9,). The dimensions are not compatible for broadcasting because the first dimension of a1 is 2 and the first dimension of a2 is 9. Therefore, a ValueError will be raised indicating that the shapes are not compatible for broadcasting.
