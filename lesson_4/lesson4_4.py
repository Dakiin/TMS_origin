x = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
y = [(3, 3, 3), (2, 2, 2), (1, 1, 1)]
z = [(2, 2, 2), (3, 3, 3), (4, 4, 4)]

len_list = len(x)
len_list_tuple = len(x[0])

res = [tuple(x[i][j]*y[i][j]*z[i][j] for j in range(len_list_tuple)) for i in range(len_list)]
print(res)
