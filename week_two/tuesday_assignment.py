"""
AJUNA MICHAEL'S ASSIGNMENT
"""

# List of cars
cars = ['audi', 'bmw', 'subaru', 'toyota', 'volkswagen', 'ford', 'mclaren']

# For looop print all items in cars list
for car in cars:
    print(car)

# Printing only 3 items in list cars
print(cars[-3:])

# function with if statement
def my_function(cars):
    if 'bmw' in cars:
        print('bmw is in the list')

my_function(cars)

carsList = ['audi', 'bmw', 'subaru', 'toyota', 'volkswagen', 'ford', 'mclaren']

# sort carsList
carsList.sort()

sortedCars = carsList;

print(sortedCars)

# forloop to print all odd numbers in range(20)
for odd_number in range(20):
    if odd_number % 2 != 0:
        print(odd_number)

# if elif
import random 

random_number = random.randint(1, 10)

if random_number % 2 != 0:
    print( str(random_number) + '' + 'odd' )
elif random_number % 2 == 0:
    print( str(random_number) + 'even')
else:
    print( str(random_number))

word = "coupe"

print(word.upper())

