#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    # Check if the matrices have the same shape along the specified axis
    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    elif axis == 1 and len(mat1) != len(mat2):
        return None

    # Concatenate along the specified axis
    if axis == 0:
        result = mat1 + mat2
    else:
        result = [mat1_row + mat2_row for mat1_row, mat2_row in zip(mat1, mat2)]

    return result
