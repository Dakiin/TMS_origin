lst = ["cat", "dog", "abrba", "father", "amama"]
print(*list(filter(lambda x: x == x[::-1], lst)))
