# Explore Special Matrices
import numpy as np

# Create a zero matrix of size 3x3
zero_matrix = np.zeros((3, 3))
print("Zero Matrix:\n", zero_matrix)

# Create an identity matrix of size 3x3
identity_matrix = np.eye(3)
print("Identity Matrix:\n", identity_matrix)

# Create a diagonal matrix with specified diagonal elements
diagonal_elements = [1, 2, 3]
diagonal_matrix = np.diag(diagonal_elements)
print("Diagonal Matrix:\n", diagonal_matrix)

# Create a random matrix of size 3x3
random_matrix = np.random.rand(3, 3)
print("Random Matrix:\n", random_matrix)

# Create a symmetric matrix
symmetric_matrix = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
print("Symmetric Matrix:\n", symmetric_matrix)

# Create a skew-symmetric matrix
skew_symmetric_matrix = np.array([[0, -1, -2], [1, 0, -3], [2, 3, 0]])
print("Skew-Symmetric Matrix:\n", skew_symmetric_matrix)
