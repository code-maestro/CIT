"""

    AJUNA MICHAEL'S ASSIGNMENT 
    (Wednesday, Week Two)

"""

# 1.Create a list that prints two values in the list together.
drivers = ['HAM', 'MAX', 'VALTERI', 'CHECO', 'CHARLES', 'MICK', 'SEB']

print(drivers[1] + ' \t ' + drivers[4])


# 2.Create a 4 dimensional list that prints out seat 130.
seats = [
    [ 10, 20, 30, 40],
    [ 50, 60, 70, 80],
    [ 90, 100, 110, 120],
    [130, 140, 150, 160]
]

print(seats[3][0])


# 3.Create a funtion that has a argument and a variable that prints out a string and integer.
import random

def my_function(randomString):
    random_number = random.randint(100, 200)
    return print(str(random_number) + randomString)

my_function(' is a random number')


# 4.Create a forloop that prints out all the items in the list.
listed_tracks = [
    ['Qatar', 21],
    ['Saudi Arabia', 5],
    ['Abu Dhabi', 12]
]

for name, date in listed_tracks:
    print(name, date)


# 5.Create a list that starts from the last item of the list and prints out the first item.
cars = ['mercedes benz', 'ferrari', 'redbull', 'alpha tauri', 'aston martin', 'HAAS']
print(cars[-1-5])
