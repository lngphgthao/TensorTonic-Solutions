def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    result = []
    for row in image:
        row_res = []
        for part in row:
            y = 0.299 * part[0] + 0.587 * part[1] + 0.114 * part[2]
            row_res.append(y)
        result.append(row_res)

    return result