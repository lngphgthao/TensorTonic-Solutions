def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    for i in range(len(matrix)):
        if sum(matrix[i]) == 0:
            continue
            
        mean = sum(matrix[i]) / len([x for x in matrix[i] if x])
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] - mean if matrix[i][j] else 0

    return matrix