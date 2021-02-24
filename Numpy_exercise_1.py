# Import np
import numpy as np

# Create an array of 10 zeros
print(np.zeros(10))

# Create an array of 10 ones
print(np.ones(10))

# Create an array of 10 fives
arr = np.ones(10)
arr[:] = 5
print(arr)

# Create an array of integers from 10 to 50
print(np.arange(10, 51))

# Create an array of even integers from 10 to 50
print(np.arange(10, 51, 2))

# Create a 3x3 matrix with values ranging from 0 to 8
print(np.arange(0, 9).reshape(3, 3))

# Create a 3x3 identity matrix
print(np.eye(3))

# Use numpy to randomly generate a number between 0 and 1
print(np.random.rand())


"""
OUTPUT:
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
[10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50]
[10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50]
[[0 1 2]
 [3 4 5]
 [6 7 8]]
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
0.15701003726532137

Process finished with exit code 0
"""
