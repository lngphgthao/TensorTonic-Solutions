import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    fpr, tpr = np.array([fpr, tpr])
    auc = 0
    
    for i in range(len(tpr) - 1):
        auc += 0.5 * (tpr[i] + tpr[i + 1]) * (fpr[i + 1] - fpr[i])

    return auc