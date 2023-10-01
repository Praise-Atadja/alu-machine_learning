#!/usr/bin/env python3

"""
   This module defines a Binomial distribution class.

"""


class Binomial:
    """
    Binomial distribution class.
    """
    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(round(n))  # Round n to the nearest integer
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Calculate p from the data
            self.p = sum(data) / len(data)
            # Calculate n based on data
            self.n = int(round(len(data) * self.p))  # Updated calculation for n
