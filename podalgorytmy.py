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

def createChildren(parentIndexes, best_cases):
    parent1 = best_cases[parentIndexes[0]]
    parent2 = best_cases[parentIndexes[1]]

    split_point = int(len(parent1) / 2)
    parent1part1 = parent1[:split_point]
    parent1part2 = parent1[split_point:]
    parent2part1 = parent2[:split_point]
    parent2part2 = parent2[split_point:]

    child1 = np.concatenate((parent1part1, parent2part2), axis=None)
    child2 = np.concatenate((parent2part1, parent1part2), axis=None)

    children = [child1, child2]
    return children