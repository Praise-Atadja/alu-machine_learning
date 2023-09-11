#!/usr/bin/env python3

def np_slice(matrix, axes={}):
    """
    Slices a numpy.ndarray along specific axes.

    Args:
        matrix (numpy.ndarray): The input matrix to be sliced.
        axes (dict): A dictionary where the key is an axis to slice along,
            and the value is a tuple representing the slice to make along that axis.

    Returns:
        numpy.ndarray: A new numpy.ndarray after applying the specified slices.

    Example:
        mat1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        result = np_slice(mat1, axes={1: (1, 3)})
        # result will be [[2 3]
        #                 [7 8]]
    """
    for axis, slicer in axes.items():
        matrix = np.take(matrix, indices=slicer, axis=axis)

    return matrix
