#!/usr/bin/env python3
import numpy as np
def np_cat(mat1, mat2, axis=0):
    concatenated_matrix = np.concatenate((mat1, mat2), axis=axis)
    return concatenated_matrix
