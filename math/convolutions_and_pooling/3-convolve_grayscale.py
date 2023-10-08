#!/usr/bin/env python3

"""that performs a same convolution on grayscale images"""


import numpy as np

def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """    Perform convolution on grayscale images with customizable padding and stride.
"""

    m, h, w = images.shape
    kh, kw = kernel.shape
    sh, sw = stride

    if padding == 'same':
        ph = int(np.ceil((h - 1) / sh))
        pw = int(np.ceil((w - 1) / sw))
        output_h = h
        output_w = w
    elif padding == 'valid':
        ph = 0
        pw = 0
        output_h = int(np.floor((h - kh) / sh) + 1)
        output_w = int(np.floor((w - kw) / sw) + 1)
    else:
        ph, pw = padding
        output_h = int(np.floor((h - kh + 2 * ph) / sh) + 1)
        output_w = int(np.floor((w - kw + 2 * pw) / sw) + 1)

    output = np.zeros((m, output_h, output_w))

    for i in range(0, h - kh + 1, sh):
        for j in range(0, w - kw + 1, sw):
            for k in range(m):
                image_patch = images[k, i:i+kh, j:j+kw]
                output[k, i//sh, j//sw] = np.sum(image_patch * kernel)

    return output
