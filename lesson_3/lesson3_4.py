n = int(input("Введите целое число!"))
total = sum([i ** 3 for i in range(1, n+1)])
print(total)


n = int(input("Введите целое число!\n"))
total = 0

if n < 0:
    print("Братишь введи неотрецательное число, зачем все портишь!?)")
    n = int(input("Вводи сюда заново целое число!\n"))
    if n >= 0:
        print("Красава так бы сразу\n")
        total = 0
        while n > 0:
            total += n ** 3
            n -= 1
        print(total)
    else:
        print("ДА ТЫ Дебил!!!")
        print("Все давай досвиданья!!!")
elif n == 0:
    print(0)
else:
    total = 0
    while n > 0:
        total += n ** 2
        n -= 1
    print(total)