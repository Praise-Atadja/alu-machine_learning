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
        self._W = np.random.randn(1, nx)
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

    def forward_prop(self, X):
        """Calculates the forward propagation of the neuron"""
        z = np.matmul(self.W, X) + self.b
        self._A = 1 / (1 + np.exp(-z))
        sigmoid = 1 / (1 + np.exp(-z))
        return self.A
