def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    word_freq = {}

    for sentence in sentences:
        for word in sentence:
            word_freq[word] = 1 if word not in word_freq else word_freq[word] + 1

    return word_freq
        