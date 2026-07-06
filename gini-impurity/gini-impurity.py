import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    N_l = len(y_left)
    N_r = len(y_right)
    N = N_l + N_r
        
    def gini(node):
        # require that a node should be a numpy array 
        node = np.array(node)
        
        labels, label_count = np.unique(node, return_counts=True) 
        proba = label_count / len(node)
        
        return 1 - np.sum(proba ** 2)
    
    return 0.0 if not N else (N_l / N) * gini(y_left) + (N_r / N) * gini(y_right)
    