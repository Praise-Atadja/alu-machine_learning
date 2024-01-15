#!/usr/bin/env python3

"""Module defines a single neuron performing binary classification"""

import numpy as np


class Neuron:
    """Each private attribute should have a corresponding getter function."""

    def __init__(self, nx):

        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.__W = np.random.randn(1, 0)
        self.__b = 0
        self.__A = 0

    def get_b(self):
        """getter method for b"""
        return self.__b

    def get_A(self):
        """getter method for A"""
        return self.__A

    def get_W(self):
        """getter method for W"""
        return self.__W
