#!/usr/bin/env python3

def add_matrices(mat1, mat2):
    """
    Adds two matrices element-wise if they have the same shape.

    Args:
        mat1 (list or nested list): The first matrix.
        mat2 (list or nested list): The second matrix.

    Returns:
        list or nested list or None: The sum of mat1 and mat2 if they have the same shape.
            Returns None if matrices have different shapes.

    Example:
        mat1 = [1, 2, 3]
        mat2 = [4, 5, 6]
        result = add_matrices(mat1, mat2)
        # result will be [5, 7, 9]
    """
    def check_shape(matrix):
        # Recursive function to check the shape of a nested list
        if isinstance(matrix[0], list):
            return [len(matrix)] + check_shape(matrix[0])
        else:
            return [len(matrix)]

    shape1 = check_shape(mat1)
    shape2 = check_shape(mat2)

    if shape1 != shape2:
        return None  # Return None if matrices have different shapes

    def add_elementwise(m1, m2):
        if isinstance(m1, list):
            return [add_elementwise(x, y) for x, y in zip(m1, m2)]
        else:
            return m1 + m2

    result = add_elementwise(mat1, mat2)

    return result
