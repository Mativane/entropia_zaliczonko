from collections import Counter
import random
import math
import numpy as np


def calculate_entropy(data):
    entropy = sum(np.negative(data) * np.log2(data))
    return entropy


def random_results(x, class_, size):
    results = []
    for i in range(x):
        result = [random.randint(1, class_) for j in range(size)]
        results.append(result)
        np.array(results)
    return results


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


def create_children(parent_indexes, best_cases):
    parent1 = best_cases[parent_indexes[0]]
    parent2 = best_cases[parent_indexes[1]]

    split_point = int(len(parent1) / 2)
    parent1part1 = parent1[:split_point]
    parent1part2 = parent1[split_point:]
    parent2part1 = parent2[:split_point]
    parent2part2 = parent2[split_point:]

    child1 = np.concatenate((parent1part1, parent2part2), axis=None)
    child2 = np.concatenate((parent2part1, parent1part2), axis=None)

    children = [child1, child2]
    return children


def mutate(children, classes):
    for child in children:
        size = len(child)
        px_to_mutate = math.ceil(size * 0.03)
        indexes = random.sample(range(0, size), px_to_mutate)
        for idx in indexes:
            old_class = child[idx]
            new_class = random.choice(classes)
            while old_class == new_class:
                new_class = random.choice(classes)
            child[idx] = new_class
    return children
