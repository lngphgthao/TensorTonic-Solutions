import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_pred, y_true = np.array([y_pred, y_true])
    N = len(y_true)
    
    return (1 / N) * np.sum(np.power(y_pred - y_true, 2))