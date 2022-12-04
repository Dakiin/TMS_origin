"""
Написать рекурсивную функцию, которая будет принимать на вход список целых чисел
и возвращать инвертированную копию этого списка (рекурсивная реализация функции reverse)
"""
lst = []


def recursive_reverse(source_list):
    """
    Your code is here
    """

    if source_list == []:
        return lst
    else:
        lst.append(source_list[-1])
        recursive_reverse(source_list[:-1])
    return lst

"""
Test
"""

source = [1, 2, 3, 4, 5]
print(source)
print(recursive_reverse(source))


#assert recursive_reverse(source) == [5, 4, 3, 2, 1]
