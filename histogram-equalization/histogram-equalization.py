def histogram_equalize(image):
    """
    Apply histogram equalization to enhance image contrast.
    """
    hist = [0] * 256
    total_pixels = len(image) * len(image[0])
    new_val = []
    
    for i in range(len(image)):
        for j in range(len(image[0])):
            hist[image[i][j]] += 1

    if max(hist) == total_pixels:
        return [[0] * len(image[0])] * len(image)
        
    cdf = [sum(hist[:i]) for i in range(1, 256+1)]
    cdf_min = min((x for x in cdf if x))

    for i in range(len(image)):
        row = []
        for j in range(len(image[0])):
            v = image[i][j]
            row.append(round(((cdf[v] - cdf_min) / (total_pixels - cdf_min)) * 255))
        new_val.append(row)
        
    return new_val
    