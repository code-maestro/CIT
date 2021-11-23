
"""

    AJUNA MICHAEL'S ASSIGNMENT (Wenesday, Week 3)

    1.Create a whileloop that prints out "I have 1-10 grapes in my hand."
    2.Create a whileloop that only prints odd numbers up to 19.
    3.Create a nested dictionary that prints (Healthy foods)vegetables and fruits.
    4.Create a function that prints only even numbers.

"""

# 1.Create a whileloop that prints out "I have 1-10 grapes in my hand.
i = 0
    
while i < 10:
    i+=1
    print("I have " + str(i) + " " + "grapes in my hand.")
    
# 2.Create a whileloop that only prints odd numbers up to 19.
odd_number = 0
while odd_number < 20:
    odd_number+=1
    if odd_number%2 != 0:
        print("\t"+str(odd_number))


# 3.Create a nested dictionary that prints (Healthy foods)vegetables and fruits.
healthy_foods = {
    "vegetables": {
        "carrots": "orange",
        "cucumber": "green",
        "tomatoes": "red"
    },
    "fruits": {
        "apples": "red",
        "bananas": "yellow",
        "pears": "green"
    }
}

print(healthy_foods)


# 4.Create a function that prints only even numbers.
def even_numbers():
    for i in range(40):
        if i%2 == 0:
            print(i)

even_numbers()
