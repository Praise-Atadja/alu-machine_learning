#!/usr/bin/env python3

"""Module defines a neural network with one
hidden layer performing binary classification:

"""


import numpy as np


class NeuralNetwork:
    """NeuralNetwork class"""

    def __init__(self, nx, nodes):
        """Constructor method"""
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be positive')
        if not isinstance(nodes, int):
            raise TypeError('nodes must be an integer')
        if nodes < 1:
            raise ValueError('nodes must be positive')
        self._W1 = np.random.normal(size=(nodes, nx))
        self._b1 = np.zeros((nodes, 1))
        self._A1 = 0
        self._W2 = np.random.normal(size=(1, nodes))
        self._b2 = 0
        self._A2 = 0
