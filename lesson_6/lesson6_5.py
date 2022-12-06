s = input()


def check_number(number):
    try:
        if "." in s:
            if "-" in s:
                print(f'Вы ввели дробное отрицательное число {float(s)}')
            else:
                print(f'Вы ввели дробное положительное число {float(s)}')
        else:
            print(f'Вы ввели дробное положительное число {int(s)}')
    except:
        print("Вы ввели не коректное число!")


check_number(s)
