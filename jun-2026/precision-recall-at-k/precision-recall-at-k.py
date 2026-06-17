def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    k_rel = len([x for x in recommended[:k] if x in relevant])
    rel = len(relevant)

    precision_k = k_rel / k
    recall_k = k_rel / rel

    return [precision_k, recall_k]