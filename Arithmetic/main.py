import numpy as np

# ************** scalar arithmetic **************

array = np.array([1,2,3,4,5])

print(array + 1) # [2 3 4 5 6]

print(array - 1) # [0 1 2 3 4]

print(array * 3) # [ 3  6  9 12 15]

print(array / 2) # [0.5 1.  1.5 2.  2.5]

print(array ** 2) # [ 1  4  9 16 25]


#  ************** Vectorized math functions **************
print(np.sqrt(array)) # [1.         1.41421356 1.73205081 2.         2.23606798]

array2  = np.array([2.33, 4.55, 1.232, 9.01])

print(np.round(array2)) # [2. 5. 1. 9.]
print(np.floor(array2)) # [2. 4. 1. 9.]

print(np.pi) # 3.141592653589793

# EXERCISE:
radius = np.array([1,2,3])
print(np.pi * radius ** 2 ) # [ 3.14159265 12.56637061 28.27433388]


# ************** Element-wise arithmetic **************
arr1 = np.array([1,2,4])
arr2 = np.array([3,4,5])

print(arr1 + arr2) # [4 6 9]
print(arr1 - arr2) # [-2 -2 -1]
print(arr1 * arr2) # [ 3  8 20]
print(arr1 / arr2) # [0.33333333 0.5        0.8       ]
print(arr1 ** arr2) # [   1   16 1024]

# ************** Comparison Operator **************

scores = np.array([91, 82,89, 78, 100, 98])

print(scores == 100) # [False False False False  True False]

print(scores >= 80) # [ True  True  True False  True  True]

scores[scores<80 ] = 0

print(scores) # [ 91  82  89   0 100  98]