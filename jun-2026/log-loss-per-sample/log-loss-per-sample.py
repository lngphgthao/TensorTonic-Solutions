import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    log_loss = []
    y_pred = np.clip(y_pred, a_min=eps, a_max=1-eps)

    for i in range(len(y_true)):
        loss = -(y_true[i] * math.log(y_pred[i]) + (1 - y_true[i]) * math.log(1 - y_pred[i]))
        log_loss.append(loss)

    return log_loss