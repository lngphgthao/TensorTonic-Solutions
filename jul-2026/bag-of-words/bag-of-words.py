import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    bow = np.zeros(len(vocab), dtype=int)
    for i in range(len(vocab)):
        bow[i] = tokens.count(vocab[i])

    return bow