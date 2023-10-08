#!/usr/bin/env python3

"""This module performs a convolution on grayscale
 images with custom padding
"""


import numpy as np

def convolve_grayscale_padding(images, kernel, padding):
    """
    Perform a convolution on grayscale images with custom padding.
    """

    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding
    output_h = h + 2 * ph - kh + 1
    output_w = w + 2 * pw - kw + 1
    output = np.zeros((m, output_h, output_w))

    # Pad the input images with zeros
    padded_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), mode='constant')

    for i in range(output_h):
        for j in range(output_w):
            for k in range(m):
                output[k, i, j] = np.sum(padded_images[k, i:i+kh, j:j+kw] * kernel)

    return output
