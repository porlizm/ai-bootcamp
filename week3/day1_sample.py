import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# print("Addition of A and B: \n", A + B)
# print("Subtraction of A and B:\n", A - B)

# #Scalar multiplication
# C = 2 * A
# print("Multiplication of A by scalar 2:\n", C)

#Matrix multiplication
D = np.dot(A, B)
print("Matrix multiplication of A and B:\n", D)