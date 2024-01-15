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
        self._W = np.random.randn(1, 0)
        self._b = 0
        self._A = 0

    def getb(self):
        """getter method for b"""
        return self._b

    def getA(self):
        """getter method for A"""
        return self._A

    def getW(self):
        """getter method for W"""
        return self._W

    nx = property(getb, getA, getW)
