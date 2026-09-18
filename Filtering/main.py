import numpy as np
# Filtering 
#           Refers to the process of selecting elements from 
#           an array that match a given condition

ages = np.array([[21,34,13,22,20,19,16,38],
                 [39,20,99,67,22,45,64,77]])

teenagers = ages[ages<18]
print(teenagers) # [13 16]

adults = ages[ages >= 18]
print(adults)  # [21 34 22 20 19 38 39 20 99 67 22 45 64 77]

adults2 = ages[(ages >= 18) & (ages<65)]
print(adults2) # [21 34 22 20 19 38 39 20 22 45 64]

adults3 = ages[(ages < 18) | (ages >= 65)]
print(adults3) # [13 16 99 67 77]

evens = ages[ages % 2 == 0]
print(evens) # [34 22 20 16 38 20 22 64]

odds = ages[ages%2!=0]
print(odds) # [21 13 19 39 99 67 45 77]

senior = np.where(ages>=18, ages, 0)
print(senior)  # [[21 34  0 22 20 19  0 38]   - original shape array
                # [39 20 99 67 22 45 64 77]]


