#!/usr/bin/env python3
import numpy as np
"""
This module contains a function that concatenates 
two matrices along a specified axis. 
It assumes that both mat1 and mat2 are 
non-empty and can be interpreted as NumPy arrays.
"""


def np_cat(mat1, mat2, axis=0):
    """Concatenate two matrices along the specified axis using NumPy.

    Args:
        mat1 (numpy.ndarray): The first matrix to concatenate.
        mat2 (numpy.ndarray): The second matrix to concatenate.
        axis (int, optional): The axis along which
        to concatenate (default is 0).

    Returns:
        numpy.ndarray: The concatenated matrix.
    """
    concatenated_matrix = np.concatenate((mat1, mat2), axis=axis)
    return concatenated_matrix
