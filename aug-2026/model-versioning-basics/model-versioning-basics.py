def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    result = sorted(models, key=lambda model: (model['accuracy'], -model["latency"], model["timestamp"]))

    return result[-1]["name"]