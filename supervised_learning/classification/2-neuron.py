#!/usr/bin/env python3

"""Module defines a single neuron performing binary classification"""


import numpy as np


class Neuron:
    """Each private attribute should have a corresponding getter function."""


    def __init__(self, nx):
        """class constructor"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter method for W"""
        return self.__W

    @property
    def b(self):
        """Getter method for b"""
        return self.__b

    @property
    def A(self):
        """Getter method for A"""
        return self.__A

    def forward_prop(self, X):
        """Calculates the forward propagation of the neuron"""
        Z = np.dot(self.__W, X) + self.__b
        sigmoid = 1 / (1 + np.exp(-Z))
        self.__A = sigmoid
        return self.__A
