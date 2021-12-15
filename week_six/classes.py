class Car:
    def __init__(self, car1, car2):
        self.car1 = car1
        self.car2 = car2

    def carColors(self):
        print("Black" + self.car1)
        print("Green " + self.car2)

cars = Car('BMW', 'Audi')

print(cars.car1)
print(cars.car2)

print(cars.carColors())