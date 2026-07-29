def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    set_a = set(set_a)
    set_b = set(set_b)

    return 0.0 if not (set_a or set_b) else len(set_a.intersection(set_b)) / len(set_a.union(set_b))