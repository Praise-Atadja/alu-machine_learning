#!/usr/bin/env python3

def summation_i_squared(n):
    # Check if n is a valid number
    if not isinstance(n, int) or n < 1:
        return None

    # Calculate the sum of squares using the formula: (n * (n + 1) * (2 * n + 1)) / 6
    # This formula efficiently computes the sum of squares of integers from 1 to n
    # without using loops or recursion.
    result = (n * (n + 1) * (2 * n + 1)) // 6

    return result
