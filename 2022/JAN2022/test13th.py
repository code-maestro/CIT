''' 

AJUNA MICHAEL ASSIGNMENT FOR THE 13TH OF JANUARY 2022


1.Inside a funtion write a python program that goes through 3 conditional statements
until it gets its final output.
2. Create a if statement using the (or)(and) operator.
3. Using the user input create a pyramid using the number 1.
4. Create a dictionary and add another item in your dictionary.
5. Create a dictionary inside a dictionary and use the nesting loop to print your output.

'''

# # 1. Inside a funtion write a python program that goes through 3 conditional statements
# carList = ["Aston Martin","Ferrari","Mercedes","Alfa Romeo","Honda", "McLaren"]

# def conditions(carName):
#     if carName in carList:
#         print(f"Nice Try {carName} is in F1")
#     elif carName not in carList:
#         print(f"Sorry, your guess {carName} is not in F1")
#     else:
#         print(" BYE 😒 ")

# conditions(input("Enter your car name: "))

# # 2. Create a if statement using the (or)(and) operator.
# def orAndOperator(a,b):
#     if a == 4 or b == 2:
#         print("True")
#     elif a == 5 and b == 6:
#         print("Could be True")
#     else:
#         print("False")

# orAndOperator(5,6)

# 3. Using the user input create a pyramid using the number 1.
def pyramid(rows):
    for i in range(rows, 1, -1):
        for s in range(0, rows - i):
            print(" ", end="")
        for j in range(i, 2 * i -1):
            print("1 ", end="")
        print()

pyramid(int(input("Enter a number: ")))

# # 4. Create a dictionary and add another item in your dictionary.
# def dictionary():
#     dict1 = {"name":"AJUNA MICHAEL","age":22,"country":"UK"}
#     dict1["state"] = "BIRMINGHAM"
#     print(dict1)

# dictionary()

# # 5. Create a dictionary inside a dictionary and use the nesting loop to print your output.
# def nestedDictionary():
#     dict = {
#         "person": {"name":"AJUNA MICHAEL","age":22,"country":"NIGERIA"},
#         "car": {"name":"Ferrari","model":"488 GTB","year":2020},
#     }

#     for key, value in dict.items():
#         for value1 in value.values():
#             print(f"{key} -> {value1}")

# nestedDictionary()