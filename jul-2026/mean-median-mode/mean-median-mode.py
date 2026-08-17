import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.array(x)
    unique, freq = np.unique(x, return_counts=True)
    mode_index = np.where(freq == np.max(freq))[0][0]
    
    return (np.mean(x), np.median(x), unique[mode_index])