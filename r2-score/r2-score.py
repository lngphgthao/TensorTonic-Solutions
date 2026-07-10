import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    if np.all(np.where(y_true == y_true[0], True, False)):
        if np.all(np.equal(y_true, y_pred)):
            return 1.0
        else:
            return 0.0
            
    det = np.power(y_true - y_pred, 2)
    nom = np.power(y_true - np.mean(y_true), 2)
    
    return 1 - np.sum(det) / np.sum(nom)