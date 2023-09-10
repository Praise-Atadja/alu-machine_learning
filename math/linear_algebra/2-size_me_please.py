#!/usr/bin/env python3
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]

shape1 = matrix_shape(matrix1)
shape2 = matrix_shape(matrix2)

print(shape1)  # Output will be [2, 3]
print(shape2)  # Output will be [2, 2, 3]
