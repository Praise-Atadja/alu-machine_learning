#!/usr/bin/env python3

"""
   This module creates a Poisson distribution class.

"""


class Poisson:
    """
    Creates poisson distribution class.

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
        result *= 2.7182818285 ** (-self.lambtha)
        return result

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of "successes."

        Args:
            k (int or float): The number of "successes."

        Returns:
            float: The CDF value for k.
        """
        k = int(k)  # Convert to integer
        if k < 0:
            return 0
        cdf_value = 0.0
        for i in range(k + 1):
            cdf_value += self.pmf(i)
        return cdf_value
