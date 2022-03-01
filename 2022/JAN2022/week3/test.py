# 25/01/2022 Assignmnt
# MICHAEL AJUNA

#  1.We have a report on the number of flu vaccinations in a class of 40 people. It has the following numbers: never:8  once: 10 twice: 4 Threetimes:6 What is the mean number of the times those people have been vaccinated?    
#  2.Create a store class that allow customers purchase items in your store.
#  3.Create a polymorphism class funtion.

# 1.We have a report on the number of flu vaccinations in a class of 40 people. It has the following numbers: never:8  once: 10 twice: 4 Threetimes:6 What is the mean number of the times those people have been vaccinated?
class Vaxed():
    allPeople = 40
    never = 8
    once = 10
    twice = 4
    threetimes = 6

print("The mean number of the times those people have been vaccinated is:", (Vaxed.once + Vaxed.twice + Vaxed.threetimes) / Vaxed.allPeople)


#  2.Create a store class that allow customers purchase items in your store.
class Store():
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
    
    def inventory(self):
        print("The items in the store are:")
        for item in self.items:
            print(item)

Store1 = Store("Store1", ["smoothie", "popcorn", "tea"])
Store1.inventory()
Store1.add_item("chips")
Store1.remove_item("tea")
Store1.inventory()

#  3.Create a polymorphism class funtion.
class Shape():
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

a = Square(4)
print(a)
print(a.area())
