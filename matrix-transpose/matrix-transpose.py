import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    row_len = len(A)
    col_len = len(A[0])
    transpose = np.zeros((col_len, row_len))
    
    for i in range(row_len):
        for j in range(col_len):
            transpose[j][i] = A[i][j]

    return np.array(transpose)
