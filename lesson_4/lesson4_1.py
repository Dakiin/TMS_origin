# 1 вариант
my_list = list(range(1, 51))
new_list = [i for i in my_list[::-1]]
print(new_list)

# 2 вариант
my_list = list(range(1, 51))
my_list = reversed(my_list)
new_list1 = [i for i in my_list]
print(new_list1)
