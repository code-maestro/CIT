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

# INHERITANCE
class Sports:
    def __init__(self, sport1, sport2):
        self.sport1 = sport1
        self.sport2 = sport2


class Second_sports(Sports):
    def sports_teams(self):
        print("Basketball" + self.sport1)
        print("Soccer" + self.sport2)

c1 = Sports("Darts", "Formula 1")
c2 = Second_sports()