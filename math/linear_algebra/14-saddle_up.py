#!/usr/bin/env python3
"Performs matrix multiplication using NumPy without loops or conditionals."
import numpy as np


def np_matmul(mat1, mat2):
    result = np.dot(mat1, mat2)
    return result
