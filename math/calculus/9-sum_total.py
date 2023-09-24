#!/usr/bin/env python3

"""
    Calculate the sum of squares of integers from 1 to n.

    Args:
        n (int): The stopping condition for the sum.

    Returns:
        int or None: The integer value of the sum of squares from 1 to n. 
                     Returns None if n is not a valid number.
"""


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
