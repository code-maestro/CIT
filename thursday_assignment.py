"""

MICHAEL AJUNA'S ASSIGNMENT

Mbarara, Uganda

"""


# FUNCTION TO PRINT NAMES AND NUMBERS
import random

def printNamesAndNumbers():
    numbers = random.randint(1,20)
    names = "mikael" + "ajuna"
    return str(numbers) + "\n" + names

print(printNamesAndNumbers())

# VARIABLE THAT TAKES ONLY 3 LETTERS OUT OF THE STRING
name = "mikael"
print(name[2:-1])

# FUNCTION WITH INPUT TO PRINT THE STRING
def printName(string):
    print(string)

printName(input("Enter Your Name : "))

# FUNCTION TO COMPARE 2 NUMBERS WITH IF STATEMENT
def compareNumbers(num1, num2):
    if num1 < num2:
        return str(num1)  + " is less than " + str(num2)

print(compareNumbers(10, 20))