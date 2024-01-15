#!/usr/bin/env python3

"""Module defines a single neuron performing binary classification"""

import numpy as np


class Neuron:
    """Each private attribute should have a corresponding getter function (no setter function)."""
    
    
    def __init__(self, nx):

        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.W = np.random.normal(size=(1, nx))
        self.b = 0
        self.A = 0
    
    def private_attributes(self, W, b, A):
        self.W = W
        self.b = b
        self.A = A

    def get__privates_attributes(self):
        return self.W, self.b, self.A
