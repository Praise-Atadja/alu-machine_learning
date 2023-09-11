#!/usr/bin/env python3
"""
This module contains a function for performing 
matrix multiplication. It assumes that both mat1 
and mat2 are non-empty and can be treated as NumPy arrays.
"""
import numpy as np


def np_matmul(mat1, mat2):
    """
    matrix multiplication
    """

    result = np.dot(mat1, mat2)
    return result
