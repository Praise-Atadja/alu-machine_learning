#!/usr/bin/env python3

"""
   This module creates a Poisson distribution class.

"""
class Poisson:
    """
    Calculates the value of the PMF for a given number of “successes”
    """
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of "successes."

        Args:
            k (int or float): The number of "successes."

        Returns:
            float: The PMF value for k.
        """
        k = int(k)  # Convert to integer
        if k < 0:
            return 0
        result = 1.0
        for i in range(1, k + 1):
            result *= self.lambtha / i
        result *= 2.71828 ** (-self.lambtha)
        return result
    
