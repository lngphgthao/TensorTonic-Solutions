import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    x = np.array(x)
    n = len(x)

    s2 = (1 / (n - 1)) * np.sum(np.power(x - np.mean(x), 2))
    s = np.sqrt(s2)

    return (s2, s)