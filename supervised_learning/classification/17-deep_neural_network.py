#!/usr/bin/env python3

"""Module defines a deep neural network performing binary classification"""


import numpy as np


class DeepNeuralNetwork:
    """DeepNeuralNetwork class"""

    def __init__(self, nx, layers):
        """Constructor method for deep neural network
        nx is the number of input features
            nx must be a positive integer
        layers is a list representing the number of nodes in each layer
            layers must be a list of positive integers
        L: number of layers in the neural network
        cache: dictionary to hold all intermediary values of the network
        weights: dictionary to hold all weights and biases of the network
            weights[layer] = [weights, biases]"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if (
            type(layers) is not list
            or len(layers) < 1
            or min(layers) < 1
        ):
            raise TypeError("layers must be a list of positive integers")
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for i in range(len(layers)):
            if i == 0:
                self.__weights['W1'] = np.random.randn(
                    layers[0], nx
                ) * np.sqrt(2 / nx)
                self.__weights['b1'] = np.zeros([layers[0], 1])
            else:
                self.__weights[
                    'W{}'.format(i + 1)
                ] = np.random.randn(
                    layers[i], layers[i - 1]
                ) * np.sqrt(2 / layers[i - 1])
                self.__weights['b{}'.format(i + 1)] = np.zeros(
                    [layers[i], 1]
                )

    @property
    def L(self):
        """Getter method for L"""
        return self.__L

    @property
    def cache(self):
        """Getter method for cache"""
        return self.__cache

    @property
    def weights(self):
        """Getter method for weights"""
        return self.__weights

    def __init__(self, nx, layers):
        """Constructor method for deep neural network"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if (
            type(layers) is not list
            or len(layers) < 1
            or min(layers) < 1
        ):
            raise TypeError("layers must be a list of positive integers")
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for i in range(len(layers)):
            if i == 0:
                self.__weights['W1'] = np.random.randn(
                    layers[0], nx
                ) * np.sqrt(2 / nx)
                self.__weights['b1'] = np.zeros([layers[0], 1])
            else:
                self.__weights[
                    'W{}'.format(i + 1)
                ] = np.random.randn(
                    layers[i], layers[i - 1]
                ) * np.sqrt(2 / layers[i - 1])
                self.__weights['b{}'.format(i + 1)] = np.zeros(
                    [layers[i], 1]
                )

    def __init__(self, nx, layers):
        """Constructor method for deep neural network"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if (
            type(layers) is not list
            or len(layers) < 1
            or min(layers) < 1
        ):
            raise TypeError("layers must be a list of positive integers")
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for i in range(len(layers)):
            if i == 0:
                self.__weights['W1'] = np.random.randn(
                    layers[0], nx
                ) * np.sqrt(2 / nx)
                self.__weights['b1'] = np.zeros([layers[0], 1])
            else:
                self.__weights[
                    'W{}'.format(i + 1)
                ] = np.random.randn(
                    layers[i], layers[i - 1]
                ) * np.sqrt(2 / layers[i - 1])
                self.__weights['b{}'.format(i + 1)] = np.zeros(
                    [layers[i], 1]
                )
