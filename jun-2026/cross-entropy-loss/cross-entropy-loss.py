import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    N = len(y_true)
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    row_i = np.arange(N)
    return -1 / N * np.sum(np.log(y_pred[row_i, y_true]))