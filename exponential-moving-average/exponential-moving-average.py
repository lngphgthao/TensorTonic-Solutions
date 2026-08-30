def exponential_moving_average(values: list, alpha: float) -> list:
    """
    Returns the exponential moving average at every position.
    """
    ema = [values[0]]

    for t in range(1, len(values)):
        ema.append(alpha * values[t] + (1 - alpha) * ema[t - 1])

    return ema