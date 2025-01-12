import numpy as np

def show_dimension(array):
    """
    Returns the number of dimensions of the given array.
    """
    return array.ndim

# Example
array = np.array([[14, 52], [35, 4]])
print("Array:", array)
print("Dimensions:", show_dimension(array))
