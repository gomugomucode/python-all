
import numpy as np

rng = np.random.default_rng() # in this default_rng() is used to create a random number generator instance. It provides better performance and more features compared to the older np.random module.

# print(rng.integers(0, 10)) # This line generates a random integer in the range [0, 10) using the integers() method of the random number generator instance (rng) and prints it to the console.

# #  we can write the above sintax like this also
# print(rng.integers(low=0, high=10)) # This line does the same thing as the previous line but uses keyword arguments (low and high) to specify the range for the random integer generation. It generates a random integer in the range [0, 10) and prints it to the console.

# #  if we want moe than 1 number we can specify the size parameter
# print(rng.integers(0, 10, size=5)) # This line generates an array of 5 random integers in the range [0, 10) using the integers() method of the random number generator instance (rng) and prints it to the console. The size parameter specifies the number of random integers to generate.


# #  to gereate random floats we can use the random() method

# print(rng.random()) # This line generates a random float in the range [0.0, 1.0) using the random() method of the random number generator instance (rng) and prints it to the console.

# # if we want to generate an array of random floats, we can specify the size parameter as well.
# print(rng.random(size=5)) # This line generates an array of 5 random floats in the range [0.0, 1.0) using the random() method of the random number generator instance (rng) and prints it to the console. The size parameter specifies the number of random floats to generate.

#  we can also specify thge high and low values for the random floats using the uniform() method
# print(rng.uniform(low=1.0, high=10.0, size=5)) # This line generates an array of 5 random floats in the range [1.0, 10.0) using the uniform() method of the random number generator instance (rng) and prints it to the console. The low and high parameters specify the range for the random float generation, and the size parameter specifies the number of random floats to generate.

# #  if we want the random number in 2d array we can specify the size as a tuple
# print(rng.uniform(low=1.0, high=10.0, size=(3, 4))) # This line generates a 2D array of random floats with 3 rows and 4 columns in the range [1.0, 10.0) using the uniform() method of the random number generator instance (rng) and prints it to the console. The low and high parameters specify the range for the random float generation, and the size parameter specifies the shape of the output array as a tuple (3, 4).

# # #  for 3d array
# print(rng.uniform(low=1.0, high=10.0, size=(2   , 3, 4))) # This line generates a 3D array of random floats with 2 blocks, 3 rows, and 4 columns in the range [1.0, 10.0) using the uniform() method of the random number generator instance (rng) and prints it to the console. The low and high parameters specify the range for the random float generation, and the size parameter specifies the shape of the output array as a tuple (2, 3, 4).

# print(rng.uniform(low=1.0, high=10.0, size=(5 ,5,5)))  # to generate the 5d array

print(rng.uniform(low=1.0 ,high =10.0 , size = (3,4,2,5,5))) # to generate the 5d array with 3 blocks, 4 rows, 2 columns, and each element is a 5x5 array of random floats in the range [1.0, 10.0). The size parameter specifies the shape of the output array as a tuple (3, 4, 2, 5, 5).