def percent_change(series: list) -> list:
    """
    Returns the fractional change between consecutive values.
    """
    return [(series[i] - series[i - 1]) / series[i - 1] if series[i - 1] else 0.0 for i in range(1, len(series))]
        