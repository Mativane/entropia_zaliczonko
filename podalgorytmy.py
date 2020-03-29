from collections import Counter
import random
import numpy as np


def calculate_entropy(data):
    entropy = sum(np.negative(data) * np.log2(data))
    return entropy


def selection(arrays, entropy, k):
    weights = []
    for array in arrays:
        occurences = [i / len(array) for i in Counter(array).values()]
        array_entropy = calculate_entropy(occurences)
        diff = abs(array_entropy - entropy)
        weights.append(1 - diff / entropy)
    result = random.choices(
        arrays,
        weights,
        k=k
    )
    return result


def random_results(x, class_, size):
    results = []
    for i in range(x):
        result = [random.randint(1, class_) for j in range(size)]
        results.append(result)
        np.array(results)
    return results
