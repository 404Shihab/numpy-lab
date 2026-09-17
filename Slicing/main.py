import numpy as np

array = np.array(
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
)

# print(array.ndim)
# print(array)

# array[start:end:step]

print(array[0:2]) #[[1 2 3 4]
                  # [5 6 7 8]]
                
print(array[1:5]) # [[ 5  6  7  8]
                   # [ 9 10 11 12]
                   # [13 14 15 16]]


print(array[0:4:2])  #[[ 1  2  3  4]
                     # [ 9 10 11 12]]


print(array[::2])   #[[ 1  2  3  4]   by default [0:end:_]
                    # [ 9 10 11 12]]

print(array[::-1]) #[[13 14 15 16]    reverse the array
                    #[ 9 10 11 12]
                    #[ 5  6  7  8]
                    #[ 1  2  3  4]]


print(array[::-2]) #[[13 14 15 16]
                   # [ 5  6  7  8]]