#Implement matrix-vector multiplication

import numpy as np

# Create a matrix A and a vector v
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([1, 0, -1])

# Perform matrix-vector multiplication
result = np.dot(M, v)

# Display the result
print("Result of matrix-vector multiplication:\n", result)