import itertools
list_1 = [1, 2, 3]
list_2 = [1, 2, 3, 4, 5]

res = [i for i in itertools.product(list_1, list_2)]
print(res)