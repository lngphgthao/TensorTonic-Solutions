def weighted_moving_average(values: list, weights: list) -> list:
    """
    Returns the weighted average of every complete window.
    """
    wma = []
    k = len(weights)
    
    for i in range(len(values) - k + 1):
        upper = sum([weights[j] * values[i + j] for j in range(k)])
        lower = sum(weights[:k])
        wma.append(upper / lower)

    return wma