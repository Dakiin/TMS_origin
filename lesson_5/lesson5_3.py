lst = [1, 1, 2, 3, 3, 4, 5, 5, 5, 5, 5, 6]


def count(l):
    dic = {}
    for i in l:
        dic[i] = dic.get(i, 0) + 1
    return dic


print(count(lst))
