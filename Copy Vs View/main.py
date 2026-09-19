import numpy as np

# ************** Copy vs View **************


# ---------------view-----------

array = np.array([1, 2, 3, 4, 5])

# Create a view of the original array.
# A view does not create a new copy of the data.
# Both arrays share the same underlying data.

array2 = array.view()

print(f"Original array: {array}")   # Original array: [1 2 3 4 5]
print(f"View array: {array2}")      # View array: [1 2 3 4 5]

array[0] = 23

# Changing the original array also changes the view
# because both arrays share the same underlying data.

print(f"Changed array: {array}")    # Changed array: [23  2  3  4  5]
print(f"Changed view: {array2}")    # Changed view: [23  2  3  4  5]


# ************** Copy **************

arr = np.array([1, 2, 3, 4, 5])

# Create a copy of the original array.
# A copy creates a new array with its own data.
# Changes made to the original array do not affect the copy.

arr2 = arr.copy()

print(f"Original arr: {arr}")        # Original arr: [1 2 3 4 5]
print(f"Copy arr: {arr2}")           # Copy arr: [1 2 3 4 5]

arr[0] = 23

# Changing the original array does not change the copy
# because they have separate data.

print(f"Changed arr: {arr}")         # Changed arr: [23  2  3  4  5]
print(f"Unchanged copy: {arr2}")     # Unchanged copy: [1 2 3 4 5]