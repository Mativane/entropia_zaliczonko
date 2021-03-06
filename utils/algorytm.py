import numpy as np
from statistics import mean

from podalgorytmy import *


def create_values_from_entropy(x, y, classes, expected_entropy):
    size = x * y

    #Obsługa przypadku gdzie classes == 1:
    if classes == 1:
        if expected_entropy == 0:
            values = np.asarray([1])
            print("Cały obrazek w jednym kolorze")
            return values
        else:
            print("Wartość niemożliwa do osiągnięcia")
            return None
    #Obsługa dziwnych parametrów wejściowych
    max_entropy_case = np.asarray([1/classes]*classes)
    print(calculate_entropy(max_entropy_case))
    if expected_entropy > calculate_entropy(max_entropy_case) or expected_entropy < 0:
        print("Wartość niemożliwa do osiągnięcia")
        return None
    if round(classes) != classes:
        print("Argument classes musi być liczbą całkowitą")
        return None
    if expected_entropy == 0:
        print("Wartość niemożliwa do osiągnięcia")
        return None
    min_entropy_case = [0] * size
    for class_ in range(classes):
        min_entropy_case[class_] = class_ 
    min_entropy = array_to_entropy(min_entropy_case)
    if min_entropy > expected_entropy:
        print("Wartość niemożliwa do osiągnięcia")
        print("Minimalna entropia dla " + str(classes) + " klas w macierzy o wielkości " + str(size) + " to " + str(min_entropy))
        return None
    
    init_cases = random_results(200, classes, size)
    classes = list(set(init_cases[0]))
    best_cases = selection(init_cases, expected_entropy, 30)
    if len(best_cases) == 1:
        print("Wśród losowych arrayów znaleziono rozwiązanie")
        print(best_cases[0])
        print(expected_entropy, array_to_entropy(best_cases[0]), set(best_cases[0]))
        return np.array(best_cases[0])

    count = 1
    best_min = min(abs(array_to_entropy(array)-expected_entropy) for array in best_cases)
    while True:
        parent_indexes = choose_parents(best_cases)
        childrens = create_children(parent_indexes, best_cases)
        m_children = mutate(childrens, classes)
        bests = choose_bests(best_cases, parent_indexes, m_children, expected_entropy)
        if len(bests) == 1:
            print("Rozwiązanie znalezione po " + str(count) + " iteracjach!")
            print(bests[0])
            print(expected_entropy, array_to_entropy(bests[0]), set(bests[0]))
            return(bests[0])
        best_cases = replace_parents_with_bests(bests, parent_indexes, best_cases)
        if count%100000 == 0:
            min_idx = np.argsort(abs(array_to_entropy(array)-expected_entropy) for array in best_cases)[0]
            print(array_to_entropy(best_cases[min_idx]))
            if best_min == array_to_entropy(best_cases[min_idx]):
                print("Przybliżone rozwiązanie znalezione po " + str(count) + " iteracjach!")
                print(best_cases[min_idx])
                print(expected_entropy, array_to_entropy(best_cases[min_idx]), set(best_cases[min_idx]))
                return best_cases[min_idx]
            best_min = array_to_entropy(best_cases[min_idx])
        count += 1
