def lag_features(series: list, lags: list) -> list:
    """
    Returns the lag feature matrix.
    """
    res = []
    
    for i in range(max(lags), len(series)):
        res.append([series[i - lag] for lag in lags])

    return res