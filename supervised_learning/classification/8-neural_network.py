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
        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = 0
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """Getter method for W1"""
        return self.__W1

    @property
    def b1(self):
        """Getter method for b1"""
        return self.__b1

    @property
    def A1(self):
        """Getter method for A1"""
        return self.__A1

    @property
    def W2(self):
        """Getter method for W2"""
        return self.__W2

    @property
    def b2(self):
        """Getter method for b2"""
        return self.__b2

    @property
    def A2(self):
        """Getter method for A2"""
        return self.__A2

    def forward_prop(self, X):
        """Calculates the forward propagation of the neural network"""
        Z1 = np.dot(self.__W1, X) + self.__b1
        sigmoid1 = 1 / (1 + np.exp(-Z1))
        self.__A1 = sigmoid1
        Z2 = np.dot(self.__W2, self.__A1) + self.__b2
        sigmoid2 = 1 / (1 + np.exp(-Z2))
        self.__A2 = sigmoid2
        return self.__A1, self.__A2

    def cost(self, Y, A):
        """Calculates the cost of the neural network"""
        x = 1.0000001 - A
        cost = -np.sum(Y * np.log(A) + (1 - Y) * np.log(x)) / Y.shape[1]
        return cost

    def evaluate(self, X):
        """Evaluates the neural network's predictions"""
        _, A2 = self.forward_prop(X)
        predictions = np.round(A2).astype(int)
        return predictions
