"""
Написать рекурсивную функцию, которая принимат на вход список целых чисел
и возвращает максимальное число в списке
"""

def recursive_max(some_list, start=0):
    """
    Your code is here
    """
    if len(some_list) == 0:
        return 0
    else:
        for i in range(len(some_list)):
            if some_list[i] > start:
                start = some_list[i]
                return recursive_max(some_list[i:], start)
    return start


"""
Test
"""

source = [2, 1, 0, 5, 7, 6, 4, 3]
print(source)
print(recursive_max(source))
assert recursive_max(source) == 7