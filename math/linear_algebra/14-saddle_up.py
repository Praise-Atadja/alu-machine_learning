#!/usr/bin/env python3
"""
np_matmul performs matrix multiplication using NumPy, 
ensuring input matrices mat1 and mat2 are non-empty ndarrays. 
No loops or conditionals.
"""
import numpy as np


def np_matmul(mat1, mat2):
    result = np.dot(mat1, mat2)
    return result
