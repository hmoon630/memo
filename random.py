from itertools import product, combinations
from operator import itemgetter

numbers = list(range(8))
number_product = list(product(numbers, repeat=2))
number_combination = list(combinations(number_product, 3))
full_product = list(product(numbers, repeat=6))
print(len(number_combination))
print(len(full_product))

a = [0, 10, 20, 30, 4, 5, 6]
b = itemgetter(1, 3, 2)
print(b(a))