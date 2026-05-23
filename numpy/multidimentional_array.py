
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


print(array.shape)  # Output: (3, 3, 3)



# chain indexing


array = np.array([[['a','b','c'],['d','e','f'] ,['g','h','i']],
                  [['j','k','l'],['m','n','o'],['p','q','r']],
                  [['s','t','u'],['v','w','x'] , ['y','z' ,' ']]])

#  to access the first element of the first layer, first column, and first row , by chain indexing we can do it like this

print(array[0, 0, 0])  # Output: a

print(array[1, 1, 1])  # Output: n

print(array[2, 2, 2])  # Output:  

word = array[0,0,0] + array[2,0,0] + array[2,0,0]
print(word)  # Output: ass

word = array[1,0,2] + array[2,0,2] + array[0,1,2] + array[0,1,2]  + array[2,2,0]
print(word)  # Output: luffy

word = array[0,2,0] +array[1,1,2] + array[1,1,0] + array[2,0,2] +  array[0,2,0] +array[1,1,2] + array[1,1,0] + array[2,0,2]  + array[0,0,2] + array[1,1,2] + array[0,1,0]+ array[0,1,1]

print(word)  # Output: gomugomucode