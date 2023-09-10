#!/usr/bin/env python3
def add_matrices2D(mat1, mat2):
    # Check if the matrices have the same shape
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    
    # Initialize an empty result matrix
    result = []

    # Iterate through the matrices and add corresponding elements
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)

    return result
