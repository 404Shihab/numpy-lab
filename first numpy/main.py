import numpy as np

# print(np.__version__)

my_list = [1,2,3,4]

my_list *=2

print(my_list)  #[1, 2, 3, 4, 1, 2, 3, 4]

array = np.array([1,2,3,4])
array *=2

print(array) #[2 4 6 8]
print(type(array)) #<class 'numpy.ndarray'>  nd- N Dimensional

