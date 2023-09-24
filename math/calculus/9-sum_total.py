#!/usr/bin/env python3

def summation_i_squared(n):
    # Check if n is a valid number
    if not isinstance(n, int) or n < 1:
        return None
    
    # Initialize the sum
    total = 0
    
    # Iterate from 1 to n and add the square of each number to the total
    for i in range(1, n + 1):
        total += i**2
    
    return total
