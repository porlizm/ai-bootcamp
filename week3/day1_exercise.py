import numpy as np

#Create two matrices A and B
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

#Perform element-wise addition and subtraction
C = A + B
D = A - B

#Display the results
print("Addition of A and B: \n", C)
print("Subtraction of A and B:\n", D)

#Scalar multiplication
E = 3 * A
print("Multiplication of A by scalar 3:\n", E)

#Matrix multiplication
F = np.dot(A, B)
print("Matrix multiplication of A and B:\n", F)