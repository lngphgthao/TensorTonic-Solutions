import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    padding = 0
    if max_len:
        padding = max_len
    else:
        for seq in seqs:
            padding = len(seq) if len(seq) > padding else padding

    for i in range(len(seqs)):
        seq_len = len(seqs[i])
        if seq_len == padding:
            continue
        elif seq_len > padding:
            seqs[i] = seqs[i][:padding]
        else:
            seqs[i] += [pad_value] * (padding - seq_len)

    return seqs