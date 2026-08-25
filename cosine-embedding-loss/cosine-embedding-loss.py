import math

def cosine_embedding_loss(x1: list, x2: list, label: int, margin: float) -> float:
    """
    Returns the cosine embedding loss as a float.
    """
    dot_prod = sum([x1[i] * x2[i] for i in range(len(x1))])
    norm_x1 = math.sqrt(sum([x1[i] ** 2 for i in range(len(x1))]))
    norm_x2 = math.sqrt(sum([x2[i] ** 2 for i in range(len(x2))]))

    cosine = dot_prod / (norm_x1 * norm_x2)

    if label == 1:
        return 1 - cosine
    else: 
        return max([0, cosine - margin])