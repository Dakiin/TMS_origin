my_list = list(range(1, 101))
my_list = [i if i % 10 == 0 else i * 2 if i % 4 == 0 else i * 2 for i in my_list]
print(my_list)