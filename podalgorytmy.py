import numpy as np
import random

def calculate_entropy(data):
    entropy = sum(np.negative(data) * np.log2(data))
    return entropy

def random_results(x, class_, size):
  results = []
  for i in range(x):
    result = [random.randint(1,class_) for j in range(size)]
    results.append(result)
    np.array(results)
  return results