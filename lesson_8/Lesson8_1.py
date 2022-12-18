import time

class Auto:
    def __init__(self, brand, age, mark, color='Red', weight=0):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('move')

    def birthday(self):
        self.age += 1

    def stop(self):
        print('stop')


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color='Red', weight=0):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color='Red', weight=0):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


obj1 = Truck("VOLVO", 3, 10, "10.000 kg")
print(obj1.brand)
print(obj1.age)
print(obj1.mark)
print(obj1.max_load)
print(obj1.color)
print(obj1.weight)
print()
obj2 = Car("AUDI", 2, 8, "250 km/h")
print(obj2.brand)
print(obj2.age)
print(obj2.mark)
print(obj2.max_speed)
print(obj2.color)
print(obj2.weight, end="\n")
