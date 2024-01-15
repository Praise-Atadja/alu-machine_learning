#!/usr/bin/env python3

import numpy as np

Class Neuron:

    """ Class that defines a single neuron performing binary classification """

    def __init__(self, nx):
        if nx is not an integer
            raise TypeError('nx must be an integer')
        if nx is less than 1
            raise ValueError('nx must be a positive integer')
        self.W = np.random.normal(size=(1, nx))
        self.b = 0
        self.A = 0