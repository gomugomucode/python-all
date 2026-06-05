
import numpy as np

rng = np.random.default_rng() # in this default_rng() is used to create a random number generator instance. It provides better performance and more features compared to the older np.random module.

# print(rng.integers(0, 10)) # This line generates a random integer in the range [0, 10) using the integers() method of the random number generator instance (rng) and prints it to the console.

#  we can write the above sintax like this also
print(rng.integers(low=0, high=10)) # This line does the same thing as the previous line but uses keyword arguments (low and high) to specify the range for the random integer generation. It generates a random integer in the range [0, 10) and prints it to the console.