#!/usr/bin/env python3

def summation_i_squared(n):
    # Check if n is a valid number
    if not isinstance(n, int) or n < 1:
        return None
    
    # Base case: If n is 1, return 1^2
    if n == 1:
        return 1
    
    # Recursive case: Calculate the sum of squares up to n
    return n**2 + summation_i_squared(n-1)
