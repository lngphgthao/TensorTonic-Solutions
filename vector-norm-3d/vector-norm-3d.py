import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    v = np.array(v)
    if v.ndim == 1:
        return np.sqrt(np.sum(np.pow(v, 2)))
    else:
        v = np.reshape(v, (-1, 3))
        return np.sqrt(np.sum(np.pow(v, 2), axis=1))