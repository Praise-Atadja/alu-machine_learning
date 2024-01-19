#!/usr/bin/env python3

"""Module defines a deep neural network performing binary classification"""


import numpy as np
import matplotlib.pyplot as plt
import pickle


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

    def forward_prop(self, X):
        """Calculates the forward propagation of the neural network"""
        self.__cache['A0'] = X
        for i in range(self.__L):
            Z = np.dot(
                self.__weights['W{}'.format(i + 1)],
                self.__cache['A{}'.format(i)]
            ) + self.__weights['b{}'.format(i + 1)]
            sigmoid = 1 / (1 + np.exp(-Z))
            self.__cache['A{}'.format(i + 1)] = sigmoid
        return sigmoid, self.__cache

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression"""
        x = 1.0000001 - A
        cost = -np.sum(Y * np.log(A) + (1 - Y) * np.log(x)) / Y.shape[1]
        return cost

    def evaluate(self, X, Y):
        """Evaluates the neural network’s predictions"""
        A, _ = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return prediction, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        """Calculates one pass of gradient descent on the neural network"""
        dz = cache["A{}".format(self.__L)] - Y
        m = Y.shape[1]
        for i in range(self.__L, 0, -1):
            db = np.sum(dz, axis=1, keepdims=True) / m
            dw = np.matmul(cache["A{}".format(i - 1)], dz.T) / m
            da = cache["A{}".format(i - 1)] * (1 - cache["A{}".format(i - 1)])
            dz = np.matmul(self.__weights["W{}".format(i)].T, dz) * da
            self.__weights["W{}".format(i)] -= alpha * dw.T
            self.__weights["b{}".format(i)] -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        """Trains the neural network"""
        if not isinstance(iterations, int):
            raise TypeError('iterations must be an integer')
        if iterations < 0:
            raise ValueError('iterations must be a positive integer')
        if not isinstance(alpha, float):
            raise TypeError('alpha must be a float')
        if alpha < 0:
            raise ValueError('alpha must be positive')
        if verbose or graph:
            if not isinstance(step, int):
                raise TypeError('step must be an integer')
            if step < 0 or step > iterations:
                raise ValueError('step must be positive and <= iterations')
        x = []
        y = []
        for i in range(iterations + 1):
            A, cache = self.forward_prop(X)
            self.gradient_descent(Y, cache, alpha)
            if i % step == 0 or i == iterations:
                cost = self.cost(Y, A)
                x.append(i)
                y.append(cost)
                if verbose:
                    print("Cost after {} iterations: {}".format(i, cost))
        if graph:
            plt.plot(x, y)
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.title('Training Cost')
            plt.show()
        return self.evaluate(X, Y)

  
    def save(self, filename):
        """ save neural network"""
        if not isinstance(filename, str):
            return
        if not filename.endswith('.pkl'):
            filename += '.pkl'
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename):
        if filename is None or not isinstance(filename, str):
            return None
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except FileNotFoundError:
            return None
