import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    v_size = len(v)
    diagonal = np.zeros((v_size, v_size))

    for i in range(v_size):
        diagonal[i][i] = v[i]

    return diagonal