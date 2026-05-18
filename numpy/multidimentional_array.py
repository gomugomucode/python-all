
import numpy as np

array = np.array('a')

print(array.ndim)  # Output: 0

array = np.array(['a','b','c'])
print(array.ndim)  # Output: 1

array = np.array([['a','b','c']])


print(array.ndim)  # Output: 2


array = np.array([['a','b','c'],
                  ['d','e','f']])
print(array.ndim)  # Output: 2

# array = np.array([[['a','b','c'],['d','e','f'] ,['g','h','i']],
#                   [['j','k','l'],['m','n','o'],['p','q','r']],
#                   [['s','t','u'],['v','w','x'] , ['y','z']]])
# in this array we get error because of the inhomogenous shape of the array.that is intha last list there are 2 element in list and inother list there are 3 element in list. so we get error because of the inhomogenous shape of the array.


array = np.array([[['a','b','c'],['d','e','f'] ,['g','h','i']],
                  [['j','k','l'],['m','n','o'],['p','q','r']],
                  [['s','t','u'],['v','w','x'] , ['y','z' ,' ']]])

print(array.ndim)  # Output: 3