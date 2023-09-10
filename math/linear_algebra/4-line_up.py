#!/usr/bin/env python3
def add_arrays(arr1, arr2):
    # Check if the arrays have the same shape
    if len(arr1) != len(arr2):
        return None
    
    # Initialize an empty result array
    result = []

    # Iterate through the arrays and add corresponding elements
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])

    return result
