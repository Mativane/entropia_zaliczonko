from collections import Counter
import random
import math
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
        if diff <= 0.03:
            return [array]
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


def mutate(children, classes):
    for child in children:
        size = len(child)
        mutation_perc = math.ceil(size * 0.03)
        indexes = random.sample(range(0, size + 1), mutation_perc)
        for idx in indexes:
            old_class = child[idx]
            new_class = random.choice(classes)
            while old_class == new_class:
                new_class = random.choice(classes)
            child[idx] = new_class
    return children
