import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(array)
print(array.shape)

arr = array.reshape(3,4)
print(arr) # [[ 1  2  3  4]
            # [ 5  6  7  8]
            # [ 9 10 11 12]]
print(arr.shape) # (3,4)


arr2 = array.reshape(3,2,2)
print(arr2) # [[[ 1  2]
            #  [ 3  4]]
            #
            # [[ 5  6]
            #  [ 7  8]]
            #
            # [[ 9 10]
            #  [11 12]]]
print(arr2.shape) # (3,2,2)

# Flatten to 1D

arr3 = arr2.reshape(-1)
print(arr3) # [ 1  2  3  4  5  6  7  8  9 10 11 12]
print(arr3.shape) # (12,)