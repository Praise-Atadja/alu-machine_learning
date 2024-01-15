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
        self._W = np.random.normal(1, nx)
        self._b = 0
        self._A = 0

    @property
    def b(self):
        """getter method for b"""
        return self._b

    @property
    def A(self):
        """getter method for A"""
        return self._A

    @property
    def W(self):
        """getter method for W"""
        return self._W

    @A.setter
    def A(self, value):
        """setter method for A"""
        self._A = value
        return self._A
