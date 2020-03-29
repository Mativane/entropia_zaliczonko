import numpy as np

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
            print("Wartość niemożliwa do osiąnięcia")
            return None
    #Obsługa dziwnych parametrów wejściowych
    max_entropy_case = np.asarray([1/classes]*classes)
    if expected_entropy > calculate_entropy(max_entropy_case) or expected_entropy < 0:
        print("Wartość niemożliwa do osiąnięcia")
        return None
    if round(classes) != classes:
        print("Argument classes musi być liczbą całkowitą")
        return None
    if expected_entropy == 0:
        print("Wartość niemożliwa do osiąnięcia")
        return None
    
    init_cases = random_results(100, classes, size)
    classes = list(set(init_cases[0]))
    best_cases = selection(init_cases, expected_entropy, 40)
    if len(best_cases) == 1:
        print("Wśród losowych arrayów znaleziono rozwiązanie")
        print(best_cases[0])
        print(expected_entropy, array_to_entropy(best_cases[0]), set(best_cases[0]))
        return np.array(best_cases[0])

    count = 1
    while True:
        parent_indexes = choose_parents(best_cases)
        childrens = create_children(parent_indexes, best_cases)
        m_children = mutate(childrens, classes)
        bests = choose_bests(best_cases, parent_indexes, m_children, expected_entropy)
        if len(bests) == 1:
            print("Rozwiązanie znalezione po " + str(count) + " iteracjach!")
            print(bests[0])
            print(expected_entropy, array_to_entropy(bests[0]), set(bests[0]))
        best_cases = replace_parents_with_bests(bests, parent_indexes, best_cases)
        count += 1
