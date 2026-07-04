import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    X = np.array(X)

    return (X - X.mean(axis=axis, keepdims=True)) / (X.std(axis=axis, keepdims=True) + eps)