import numpy as np

def calculate_entropy(data):
    entropy = sum(np.negative(data) * np.log2(data))
    return entropy