#!/usr/bin/env python3
"""
Function that creates the training operation
for the neural network
"""


import tensorflow as tf


def create_train_op(loss, alpha):
    """
    Creates the training operation for the network

    parameters:
        loss [tensor]: loss of the network's prediction
        alpha [float]: learning rate

    returns:
        operation that trains the network using gradient descent
    """
    optimizer = tf.optimizers.SGD(learning_rate=alpha)
    return optimizer.minimize(loss)
