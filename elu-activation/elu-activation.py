def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    import math
    
    return [y if y > 0 else alpha * (math.exp(y) - 1) for y in x] 