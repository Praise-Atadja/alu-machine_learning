#!/usr/bin/env python3

"""Module defines a single neuron performing binary classification"""

import numpy as np


class Neuron:
    """ Class that defines a single neuron performing binary classification  (Based on 0-neuron.py)"""

    def __init__(self, nx):

        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.W = np.random.normal(size=(1, nx))
        self.b = 0
        self.A = 0
    
    """Each private attribute should have a corresponding getter function (no setter function)."""
    
    def __init__(self, private_attributes):
        self.__private_attributes = private_attributes

    def get_private_attributes(self):
        return self.__private_attributes
