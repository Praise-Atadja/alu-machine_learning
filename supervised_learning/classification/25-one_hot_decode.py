#!/usr/bin/env python3

"""Encodes a numeric label vector into a one-hot matrix"""


import numpy as np


def one_hot_decode(one_hot):
    """Encodes a numeric label vector into a one-hot matrix"""
    if not isinstance(one_hot, np.ndarray):
        return None
    if len(one_hot.shape) != 2:
        return None
    if not np.all((one_hot == 0) | (one_hot == 1)):
        return None
    return np.argmax(one_hot, axis=0)
