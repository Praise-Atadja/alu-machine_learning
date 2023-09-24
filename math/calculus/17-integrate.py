#!/usr/bin/env python3

def poly_integral(poly, C=0):
    # Check if poly is a valid list of coefficients
    if not isinstance(poly, list) or not all(isinstance(coeff, (int, float)) for coeff in poly):
        return None
    
    # Check if C is a valid integer
    if not isinstance(C, int):
        return None
    
    # Initialize the result list with C as the constant term
    result = [C]
    
    # Iterate through the coefficients in poly and integrate each term
    for i, coeff in enumerate(poly):
        if isinstance(coeff, int):
            # If the coefficient is an integer, perform integer division
            result.append(coeff // (i + 1))
        else:
            # If the coefficient is a float, perform regular division
            result.append(coeff / (i + 1))
    
    # Remove any trailing zeros
    while result and result[-1] == 0:
        result.pop()
    
    # Add 0 as the constant term if the result is empty
    if not result:
        result.append(0)
    
    return result
