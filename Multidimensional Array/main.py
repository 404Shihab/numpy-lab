import numpy as np

array = np.array('S') 

print(array.ndim) # 0 D
#--------------------------

array = np.array(['a'])

print(array.ndim) # 1

array = np.array(['a', 'b', 'c'])

print(array.ndim) # 1

#----------------------------

array = np.array([
    ['a','b','c'],
    ['b','c','d'],
    ['e','f','g']
])
print(array.ndim) # 2


#------------------------------

array = np.array([
    [['A','B','C'],['D','E','F'],['G','H','I']],
    [['J','K','L'],['M','N','O'],['P','Q','R']],
    [['S','T','U'],['V','W','X'],['Y','Z',' ']]
])

# accessing element:
print(array[0][0][0]) # A  chain indexing
print(array[0,0,0]) # A  multidimensional indexing (it is more concise and efficient)
print(array[1][1][2]) # O


word = array[0,0,0] + array[0,2,2] + array[2,0,2] + array[0,0,1]  # string concatenation: Joining multiple strings using the + operator.
print(word)  # AIUB

print(array.ndim) # 3

print(array.shape) # (3, 3, 3)



# 3 elements in each row (columns)
# 3 rows in each block
# 3 blocks

array = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]])

print(array.ndim)   # 3
print(array.shape)  # (2, 3, 4)

