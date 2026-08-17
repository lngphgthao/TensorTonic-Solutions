import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    max_count = 0
    max_index = y_train[0]
    
    for i in np.unique(y_train):
        count = y_train.count(i)
        if count > max_count:
            max_count = count
            max_index = i

    return np.full(len(X_test), max_index)