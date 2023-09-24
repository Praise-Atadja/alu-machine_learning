#!/usr/bin/env python3

def poly_derivative(poly):
    # Check if poly is a valid list of coefficients
    if not isinstance(poly, list) or not all(isinstance(coeff, (int, float)) for coeff in poly):
        return None
    
    # Calculate the derivative of the polynomial
    derivative = []
    for i in range(1, len(poly)):
        # Multiply each coefficient by its corresponding power of x
        derivative.append(poly[i] * i)
    
    # If the derivative is all zeros, return [0]
    if all(coeff == 0 for coeff in derivative):
        return [0]
    
    return derivative

