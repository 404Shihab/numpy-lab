import numpy as np

# ************** Copy vs View **************

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