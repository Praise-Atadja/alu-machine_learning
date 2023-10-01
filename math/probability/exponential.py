#!/usr/bin/env python3

"""
   This module creates a class Exponential.
"""


class Exponential:
    """
    Exponential distribution class.
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
            self.lambtha = 1 / (sum(data) / len(data))

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given time period.

        Args:
            x (float): The time period.

        Returns:
            float: The PDF value for x.
        """
        if x < 0:
            return 0
        pdf_value = self.lambtha * 2.7182818285 ** (-self.lambtha * x)
        return pdf_value

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given time period.

        Args:
            x (float): The time period.

        Returns:
            float: The CDF value for x.
        """
        if x < 0:
            return 0
        cdf_value = 1 - 2.7182818285 ** (-self.lambtha * x)
        return cdf_value
