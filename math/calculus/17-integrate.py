#!/usr/bin/env python3

def poly_integral(poly, C=0):
    # Check if poly is a valid list of coefficients
    if not isinstance(poly, list) or not all(isinstance(coeff, (int, float)) for coeff in poly):
        return None
    
    # Check if C is a valid integer
    if not isinstance(C, int):
        return None
    
    # Calculate the integral of the polynomial
    integral = [C]  # Initialize the result list with the integration constant C
    for i, coeff in enumerate(poly):
        if isinstance(coeff, int):
            # If the coefficient is an integer, perform integer division
            integral.append(coeff // (i + 1))
        else:
            # If the coefficient is a float, perform regular division
            integral.append(coeff / (i + 1))
    
    return integral
