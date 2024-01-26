#!/usr/bin/env python3
"""
Function  calculates the softmax cross-entropy loss of a prediction
"""


import tensorflow as tf


def calculate_loss(y, y_pred):
    """
    Calculates the softmax cross-entropy loss of a prediction

    parameters:
        y [tf.placeholder]: placeholder for labels of the input data
        y_pred [tensor]: contains network's predictions

    returns:
        tensor containing loss of the prediction
    """
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
        labels=y,
        logits=y_pred
    ))
    return loss
