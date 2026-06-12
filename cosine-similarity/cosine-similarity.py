import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    return 0 if not (np.linalg.norm(a) and np.linalg.norm(b)) else np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))