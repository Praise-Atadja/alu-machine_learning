#!/usr/bin/env python3
"""Moduke defines a neural network
with one hidden layer performing binary classification"""


import numpy as np


class NeuralNetwork:
    """NeuralNetwork class"""

    def __init__(self, nx, nodes):
        """constructor method for neural network"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self._W1 = np.random.randn(nodes, nx)
        self._b1 = np.zeros([nodes, 1], dtype=float)
        self._A1 = 0
        self._W2 = np.random.randn(1, nodes)
        self._b2 = 0
        self._A2 = 0

    @property
    def W1(self):
        """getter method for W1"""
        return self._W1

    @property
    def b1(self):
        """getter method for b1"""
        return self._b1

    @property
    def A1(self):
        """getter method for A1"""
        return self._A1

    @property
    def W2(self):
        """getter method for W2"""
        return self._W2

    @property
    def b2(self):
        """getter method for b2"""
        return self._b2

    @property
    def A2(self):
        """getter method for A2"""
        return self._A2
