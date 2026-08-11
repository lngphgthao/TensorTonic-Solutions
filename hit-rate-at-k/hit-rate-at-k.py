def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    if len(recommendations) == 0:
        return 0.0 
    
    total = len(recommendations)
    hit = sum([1 if ground_truth[i][0] in recommendations[i][:k] else 0 for i in range(total)])

    return hit / total
        