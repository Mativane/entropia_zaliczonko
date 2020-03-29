from algorytm import create_values_from_entropy
import matplotlib.pyplot as plt
import numpy as np

#DLA STAREJ WERSJI!!
"""
result = create_values_from_entropy(8, 8, 1, 0)
result = create_values_from_entropy(8, 8, 1, 1) #nieprawdiłowy
result = create_values_from_entropy(8, 8, 2, 0) #nieprawdiłowy
result = create_values_from_entropy(8, 8, 2, 100) #nieprawdiłowy

result = create_values_from_entropy(8, 8, 2, 1)
result = create_values_from_entropy(8, 8, 3, 1.2)
"""

result = create_values_from_entropy(40, 40, 8, 2.3).reshape(40,40)

plt.imshow(result)
plt.show()