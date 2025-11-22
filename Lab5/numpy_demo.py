# --------------------------------- Example 1 -------------------------------- #

# import numpy as np

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix*3)

# np_matrix = np.array(matrix)
# print(np_matrix*3)

# --------------------------------- Example 2 -------------------------------- #
import numpy as np

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Matrix:")
print(matrix)

# Transpose matrix
print("Transposed Matrix:")
print(matrix.T)

# Element-wise multiplication
result = matrix * 3

print("Matrix Multiplication Result:")
print(result)