import json

d = {
    111111: ("ANDREY", 30),
    222222: ("DIMA", 29),
    333333: ("ZINA", 28),
    444444: ("SANYA", 33),
    555555: ("FEDOR", 56)
}

with open("d_file.json", "w") as file:
    json.dump(d, file)
