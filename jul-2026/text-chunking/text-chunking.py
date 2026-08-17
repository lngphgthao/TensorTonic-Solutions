def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    if not tokens:
        return tokens
        
    num_tokens = len(tokens) - (len(tokens) % chunk_size)
    step = chunk_size - overlap
    chunks = []
    
    for i in range(0, num_tokens, step):
        chunks.append(tokens[i:i+chunk_size])

    return [tokens] if not chunks else chunks