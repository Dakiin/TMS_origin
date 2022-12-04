# #1 ЗАДАНИЕ
# #1-задание 1-й вариант
s = input("ВВодим строку из 2-х слов\n")
lst = s.split()
z = "!" + lst[1] + " ! " + lst[0] + "!"
print(z)

#1-задание 2-й вариант
char = "!"
k = char + s.replace(" ", " ! ") + char
print(k)

#1-задание 3-й вариант
w = "! !"
print(w.replace(" ", s).replace(" ", " ! "))
