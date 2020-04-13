from algorytm import create_values_from_entropy
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

#DLA STAREJ WERSJI!!
"""
result = create_values_from_entropy(8, 8, 1, 0)
result = create_values_from_entropy(8, 8, 1, 1) #nieprawdiłowy
result = create_values_from_entropy(8, 8, 2, 0) #nieprawdiłowy
result = create_values_from_entropy(8, 8, 2, 100) #nieprawdiłowy

result = create_values_from_entropy(8, 8, 2, 1)
result = create_values_from_entropy(8, 8, 3, 1.2)
"""

shape = (10, 10)
import time
start = time.time()
result = create_values_from_entropy(*shape, 4, 1.).reshape(shape)
# result = np.array((list(result)*4)).reshape(20,20)
process_time = time.time() - start
print('Czas: ', process_time/60)
# plt.imshow(result)
# plt.legend()
# plt.show()

values = np.unique(result.ravel())

plt.figure(figsize=(9,7))
im = plt.imshow(result, extent=[0,10, 0, 10])
colors = [im.cmap(im.norm(value)) for value in values]
patches = [mpatches.Patch(color=colors[i], label="Class {l}".format(l=values[i]+1)) for i in range(len(values))]
plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plt.grid(b=True, which='major', color='#999999', linestyle='-')
plt.show()