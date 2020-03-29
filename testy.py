from algorytm import create_values_from_entropy

#DLA STAREJ WERSJI!!

result = create_values_from_entropy(8, 8, 1, 0)
result = create_values_from_entropy(8, 8, 1, 1) #nieprawdiłowy
result = create_values_from_entropy(8, 8, 2, 0) #nieprawdiłowy
result = create_values_from_entropy(8, 8, 2, 100) #nieprawdiłowy

result = create_values_from_entropy(8, 8, 2, 1)
result = create_values_from_entropy(8, 8, 3, 1.2)