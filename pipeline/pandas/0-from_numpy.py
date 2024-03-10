#!/usr/bin/env python3
import pandas as pd
import numpy as np

def from_numpy(array):
    """Converts the numpy array to a pandas DataFrame"""
    df = pd.DataFrame(array)
    
    """Generates column labels in alphabetical order and capitalize them"""
    columns = [chr(65 + i) for i in range(df.shape[1])]
    
    """Assign the generated column labels to the DataFrame"""
    df.columns = columns
    
    """Step 4: Returns the DataFrame"""
    return df