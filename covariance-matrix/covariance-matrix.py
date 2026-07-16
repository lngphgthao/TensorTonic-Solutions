import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.array(X)
    if X.shape[0] < 2 or X.ndim == 1:
        return None
        
    X = X - np.mean(X, axis=0)

    return 1 / (len(X) - 1) * X.T @ X
    