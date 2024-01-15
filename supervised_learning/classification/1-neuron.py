#!/usr/bin/env python3

"""Module defines a single neuron performing binary classification"""

import numpy as np


class Neuron:
    """Each private attribute should have a corresponding getter function."""

    def __init__(self, nx,):

        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.__W = np.random.normal(1, nx)
        self.__b = 0
        self.__A = 0

     """Each private attribute should have a corresponding getter function."""
    def get__b(self):
        """getter method for __b"""
        return self.__b

    def get__A(self):
        """getter method for __A"""
        return self.__A

    def get__W(self):
        """getter method for __W"""
        return self.__W
