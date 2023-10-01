#!/usr/bin/env python3

class Poisson:
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
            self.lambtha = sum(data) / len(data)

# Example usage:
# Create an instance of Poisson with lambtha specified
poisson1 = Poisson(lambtha=2.5)
print(poisson1.lambtha)  # Output: 2.5

# Create an instance of Poisson with data to estimate lambtha
data_points = [1, 2, 3, 4, 5]
poisson2 = Poisson(data_points)
print(poisson2.lambtha)  # Output: 3.0
