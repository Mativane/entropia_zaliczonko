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
        array_entropy = array_to_entropy(array)
        diff = abs(array_entropy - entropy)
        if diff <= 0.01:
            return [array]
        weights.append(1 - diff / entropy)
    result = random.choices(
        arrays,
        weights,
        k=k
    )
    return result


def choose_parents(parents):
    chosen = random.sample(range(len(parents)),2)
    return chosen


def create_children(parent_indexes, best_cases):
    parent1, parent2 = get_parents(best_cases, parent_indexes)
    classes = set(parent1)
    split_point = int(len(parent1) / 2)
    parent1part1 = parent1[:split_point]
    parent1part2 = parent1[split_point:]
    parent2part1 = parent2[:split_point]
    parent2part2 = parent2[split_point:]

    child1 = np.concatenate((parent1part1, parent2part2), axis=None)
    child2 = np.concatenate((parent2part1, parent1part2), axis=None)

    children = []
    for child in [child1, child2]:
        if set(child) == classes:
            children.append(child)

    return children


def mutate(children, classes):
    mutated_children = []
    for child in children:
        size = len(child)
        px_to_mutate = math.ceil(size * 0.05)
        indexes = random.sample(range(0, size), px_to_mutate)
        for idx in indexes:
            old_class = child[idx]
            new_class = random.choice(classes)
            while old_class == new_class:
                new_class = random.choice(classes)
            child[idx] = new_class
        if list(set(child)) == classes:
            mutated_children.append(child)
    return mutated_children


def choose_bests(best_cases, parent_idx, children: list, entropy):
    parents = get_parents(best_cases, parent_idx)
    current_cases = children.copy()
    current_cases.extend(parents)
    cases_entropy = []
    for array in current_cases:
        diff = abs(array_to_entropy(array) - entropy)
        if diff <= 0.01:
            return [array]
        cases_entropy.append(diff)
    best_arrays = []
    min_indexes = np.argsort(cases_entropy)[:2]
    best_arrays = [current_cases[idx] for idx in min_indexes]
    return best_arrays


def get_parents(cases, indexes):
    parent1 = cases[indexes[0]]
    parent2 = cases[indexes[1]]
    return parent1, parent2


def array_to_entropy(array):
    occurences = [i / len(array) for i in Counter(array).values()]
    return calculate_entropy(occurences)


def replace_parents_with_bests(bests, parent_indexes, best_cases):
    best_cases[parent_indexes[0]] = bests[0]
    best_cases[parent_indexes[1]] = bests[1]
    return best_cases
