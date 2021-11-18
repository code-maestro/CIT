"""

    AJUNA MICHAEL'S ASSIGNMENT 
    (Wednesday, Week Two)

"""


# 4D list, that prints out the number 33
listed_numbers = [
    [20, 11, 12, 13],
    [20, 21, 22, 23],
    [30, 31, 32, 33],
    [40, 41, 42, 43]
]

print(listed_numbers[2][3])

# 2.Create a forloop that prints out your name 3 times.
for i in range(3):
    print("mikael ajuna")

# 3.Create a function that use the if statement. 
def my_function(input_string):
    if input_string == "max":
        print("2021 CHAMP")
    else:
        print("NOT MAX")

my_function(input("Enter your champ: \n"))

# 4.Create a forloop that print out all even numbers in a range of 20.
for i in range(20):
    if i % 2 == 0:
        print(str(i) + "\n")

# # 5.Create a if statement using the ELIF statement. 
if input("Enter your champ: \n") == "max":
    print("2021 CHAMP")
elif input("Enter your champ: \n") == "mikael":
    print("2021 CHAMP")
else:
    print("NOT MAX WRONG CHOICE SON")


# 6.Create a variable that change a name from Upper case to lower case letters.
name = input("Enter your name in caps: \n")
print(name.lower())