def fuct(n):
    if n == 0:
        return 1
    return fuct(n - 1) * n


print(fuct(5))
