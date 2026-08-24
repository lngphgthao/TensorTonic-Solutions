def differencing(series: list, order: int) -> list:
    """
    Returns the series after the requested differencing order.
    """
    x = [series[i] - series[i - 1] for i in range(1, len(series))]

    for _ in range(order - 1):
        x = [x[i] - x[i - 1] for i in range(1, len(x))]

    return x