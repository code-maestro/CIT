# MICHAEL AJUNA 9TH FEBUARY 2022 ASSIGNMENT

# # 1.Create a function using the else and elif statement to get your output.
# def fun():
#     number = input("Enter a number: ")
#     if int(number) % 2 == 0:
#         print("The number is even")
#     elif int(number) % 2 == 1:
#         print("The number is odd")
#     else:
#         print("The number is not a number")

# fun()

# 2.Create a nesting dictionary
dict = {
    "name": "Michael",
    "age": "21",
    "address": {
        "street": "Tab Road",
        "city": "Kampala"
    }
}

print(dict)
for keys, values in dict.items():
    print(keys, values)

    
# 3.Create a whileloop that prints only odd numbers
import random
x = 0
while x < random.randint(0, 20):
    if x % 2 != 0:
        print(x)
    x += 1

# You need to make a function that converts a foot value to inches. (1 foot has 12 inches). Defind convert() function, that takes the foot value as an argument and outputs the inches.
def convert(foot):
    return print(foot, "in Inches = ", str(foot * 12), "Inches")

convert(int(input("Enter foot value to convert inches: ")))

# 5. Create a list and and find out the length of that list.
import random as r

random_number_list = []
for i in range(r.randint(1, 10)):
    random_number_list.append(r.randint(2,5))

print(random_number_list)
print(len(random_number_list))