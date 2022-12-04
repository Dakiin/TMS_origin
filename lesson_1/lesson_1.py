# # lesson 1
# №1
a = int(input())
b = int(input())

sum = a + b
dif = a - b
mul = a * b
if b != 0:
    div = a / b
else:
    b = int(input("Введите число не равное 0"))
    div = a / b
mod = a % b
int_div = a // b

print(sum, dif, mul, div, mod, int_div)

# №2
x = 17 / 2 * 3 + 2 # x = (17 / 2) * 3 + 2
x = 2 + 17 / 2 * 3 # x = 2 + (17 / 2) * 3
x = 19 % 4 + 15 / 2 * 3 # x = 19 % 4 + (15 / 2 * 3)
x = (15 + 6) - 10 * 4 # x = (15 + 6) - (10 * 4)
x = 17 / 2 % 2 * 3 ** 3 # x = 17 / 2 % 2 * (3 ** 3)

# №3

x = int(input())
y = int(input())
res = (abs(x) - abs(y)) / (1 + abs(x * y))


#slices
s = "aaaaaBccBddBeeBffBggB"
print(s[5::3])

s = "AAAABBBBCCCCDDDDFFFF"
print(s[:5] + s[5:9] + s[9:13] + s[13:])

s = "PYTHON"
print(s[::-1])