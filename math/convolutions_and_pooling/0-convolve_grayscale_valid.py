#!/usr/bin/env python3

"""This module performs a valid convolution on grayscale images:"""
import numpy as np

def convolve_grayscale_valid(images, kernel):
    m, h, w = images.shape
    kh, kw = kernel.shape
    output_h = h - kh + 1
    output_w = w - kw + 1
    output = np.zeros((m, output_h, output_w))

    for i in range(m):
        for j in range(output_h):
            for k in range(output_w):
                patch = images[i, j:j+kh, k:k+kw]
                output[i, j, k] = np.sum(patch * kernel)

    return output
