import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v = np.array(v)

    if v.ndim == 1:
        norm = np.sqrt(np.sum(np.pow(v, 2)))
    else:
        v = np.reshape(v, (-1, 3))
        norm = np.sqrt(np.sum(np.pow(v, 2), axis=1, keepdims=True))
        
    return np.where(norm != 0, v / norm, 0)