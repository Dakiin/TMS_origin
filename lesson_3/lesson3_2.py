name = input()
age = input()

if age.isdigit() and 0 < int(age) < 10:
    print(f"Привет шкет {name}")
elif age.isdigit() and 9 < int(age) <= 18:
    print(f"Как жизнь {name}")
elif age.isdigit() and 18 < int(age) < 100:
    print(f"Что желаете {name}")
elif age.isdigit() and 100 < int(age):
    print(f"{name} вы лжете в наше время столько не живут")
else:
    print("Ошибка повторите ввод")