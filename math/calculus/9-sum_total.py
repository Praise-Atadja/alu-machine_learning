#!/usr/bin/env python3

def summation_i_squared(n):
    # Check if n is a valid number
    if not isinstance(n, int) or n < 1:
        return None
    
    # Calculate the sum of squares using the formula
    result = (n * (n + 1) * (2 * n + 1)) // 6
    
    return result
