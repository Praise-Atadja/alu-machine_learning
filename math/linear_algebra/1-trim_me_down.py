#!/usr/bin/env python3
def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1 (list or nested list): The first matrix.
        mat2 (list or nested list): The second matrix.
        axis (int): The axis along which to concatenate. Default is 0 (vertical concatenation).

    Returns:
        list or nested list or None: The concatenated matrix or None if concatenation is not possible.

    Example:
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[5, 6], [7, 8]]
        result = cat_matrices(mat1, mat2)
        # result will be [[1, 2], [3, 4], [5, 6], [7, 8]]
    """
    def check_shape(matrix):
        # Recursive function to check the shape of a nested list
        if isinstance(matrix[0], list):
            return [len(matrix)] + check_shape(matrix[0])
        else:
            return [len(matrix)]

    shape1 = check_shape(mat1)
    shape2 = check_shape(mat2)

    if len(shape1) != len(shape2):
        return None  # Return None if dimensions don't match

    if axis < 0 or axis >= len(shape1):
        return None  # Invalid axis value

    if shape1[axis] != shape2[axis]:
        return None  # Return None if dimensions along the specified axis don't match

    def concatenate_matrices(m1, m2):
        if isinstance(m1[0], list):
            return [concatenate_matrices(x, y) for x, y in zip(m1, m2)]
        else:
            return m1 + m2

    result = concatenate_matrices(mat1, mat2)

    return result
