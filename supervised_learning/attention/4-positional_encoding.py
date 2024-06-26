#!/usr/bin/env python3
"""
4-positional_encoding.py
"""
import numpy as np


def positional_encoding(max_seq_len, dm):
    """function that computes the positional encoding vector"""

    # Computes the angles for the positional encoding
    angle_rads = get_angles(np.arange(max_seq_len)[:, np.newaxis],
                            np.arange(dm)[np.newaxis, :],
                            dm)

    # apply sin to even indices in the array; 2i
    angle_rads[:, 0::2] = np.sin(angle_rads[:, 0::2])

    # apply cos to odd indices in the array; 2i+1
    angle_rads[:, 1::2] = np.cos(angle_rads[:, 1::2])

    pos_encoding = angle_rads[np.newaxis, ...]

    return pos_encoding[0]


def get_angles(position, i, dm):
    """function that computes the angles for the positional encoding"""

    angle_rates = 1 / np.power(10000, (2 * np.floor(i / 2)) / np.float32(dm))

    return position * angle_rates
