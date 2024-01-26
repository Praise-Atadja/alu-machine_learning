#!/usr/bin/env python3
"""
Function that calculates the accuracy of a prediction:
"""


import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    y is a placeholder for the labels of the input data
    y_pred is a tensor containing the network predictions
    Returns: a tensor containing the decimal accuracy of the prediction
    hint: accuracy = correct_predictions / all_predictions
    """
    T= tf.argmax(y, axis=1)
    correct_predictions = tf.equal(tf.argmax(y_pred, axis=1), T)
    accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))
    return accuracy
