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
        Z = np.dot(self._W, X) + self._b
        sigmoid = 1 / (1 + np.exp(-Z))
        self._A = sigmoid
        return self._A

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression"""
        x = 1.0000001 - A
        cost = -np.sum(Y * np.log(A) + (1 - Y) * np.log(x)) / Y.shape[1]
        return cost

    def evaluate(self, X, Y):
        """Evaluates the neuron’s predictions"""
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return prediction, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Calculates one pass of gradient descent on the neuron"""
        dz = A - Y
        dw = np.dot(X, dz.T) / X.shape[1]
        db = np.sum(dz) / X.shape[1]
        self._W = self._W - alpha * dw.T
        self._b = self._b - alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        """Trains the neuron"""
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
    cost_list = []
    for i in range(iterations + 1):
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        if verbose and i % step == 0:
            print('Cost after {} iterations: {}'.format(i, cost))
            cost_list.append(cost)
        if i < iterations:
            self.gradient_descent(X, Y, A, alpha)
    if graph:
        plt.plot(np.arange(0, iterations + 1), cost_list)
        plt.xlabel('iteration')
        plt.ylabel('cost')
        plt.title('Training Cost')
        plt.show()
    self.evaluate(X, Y)
