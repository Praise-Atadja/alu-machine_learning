#!/usr/bin/env python3
def matrix_transpose(matrix):
    # Calculate the number of rows and columns in the input matrix
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    # Create a new matrix with swapped dimensions
    transpose_matrix = [[0] * num_rows for _ in range(num_columns)]

    # Populate the transpose matrix
    for i in range(num_rows):
        for j in range(num_columns):
            transpose_matrix[j][i] = matrix[i][j]

    return transpose_matrix
