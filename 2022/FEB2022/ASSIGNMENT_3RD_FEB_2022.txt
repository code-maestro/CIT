# ASSIGNMENT FOR FEBUARY 3RD 2022
# MICHAEL AJUNA

# 1.Create "two" 2-D array and divide each array of both 2-D array.
import numpy as np
first_arr = np.array([[2,4],[6, 8]])
second_arr = np.array([[1,3],[5, 7]])

print(first_arr[0]/second_arr[0])
print(first_arr[1]/second_arr[1])

# 2.Create a game using if statements and user inputs.
import random
print("\n\n\tWelcome to the ROCK - PAPPER - SCISSOR game! \n")

user_input = input("\tEnter guess: ")

choices = ["ROCK", "PAPER", "SCISSOR"]

computer_guess = random.choice(choices)

if computer_guess == user_input.upper():
    print("\tYou chose", user_input.upper(), "\t Computer chose", computer_guess , "\n\tIt's a tie!")
elif user_input.upper() == "ROCK" and computer_guess == "PAPER" or user_input.upper() == "PAPER" and computer_guess == "SCISSORS" or user_input.upper() == "SCISSORS" and computer_guess == "ROCK":
    print("\tYou chose", user_input.upper(), "\n\t Computer chose", computer_guess , "\n\tYou lose!")
else:
    print("\tYou chose", user_input.upper(), "\n\t Computer chose", computer_guess , "\n\tYou win!")


# 3.Create a list and pop and replace an element out of your list, then convert it to a tuple.
cars = ["BMW", "AUDI", "MERCEDES", "TOYOTA", "HONDA"]
print("\n Original list: ", cars)
cars.pop(2)
print("\n List after pop: ",cars)
cars.insert(2, "PORSCHE")
print("\n List after replacing",cars)

print("\n Converting list to tuple: ", tuple(cars) , "\n")

# 4.Create a "L" pattern object using using the letter "L"
for i in range(4):
    print("L")
    if i == 3:
        print("L " * 3, "\n")


# 5.Create a while loop that prints your name 10 times.
i = 0
while i < 10:
    print("mikael")
    i += 1

