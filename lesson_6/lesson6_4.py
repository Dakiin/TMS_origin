from datetime import datetime


def decor(fun):
    def wrap():
        start_time = datetime.now()
        print(f"Функция начала работать в ----> {start_time}")
        fun()
        end_time = datetime.now()
        res = end_time - start_time
        print(f"Функция отработала за {res}")

    return wrap


@decor
def hello():
    print(f"Hello world")


@decor
def sum_list_in_range():
    print(sum([i for i in range(1, 30)]))


hello()
print()
sum_list_in_range()

