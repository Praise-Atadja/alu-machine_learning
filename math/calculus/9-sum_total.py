#!/usr/bin/env python3

"""Module for calculating the sum of squares of integers."""

def summation_i_squared(n):
    # Check if n is a valid number
    if not isinstance(n, int) or n < 1:
        return None

    # Calculate the sum of squares using the formula
    # This formula efficiently computes the sum of squares of integers
    # without using loops or recursion.
    result = (n * (n + 1) * (2 * n + 1)) // 6

    # Return the result, which is the sum of squares
    return result
