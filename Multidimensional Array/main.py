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


