import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    if not y:
        return 0.0
        
    p = np.zeros(max(y) + 1)
    for sample in y:
        p[sample] += 1
    p /= len(y)
    
    safe_p = np.clip(p, 1e-15, None)  
    entropy = (-p * np.emath.log2(safe_p)).sum()

    return entropy