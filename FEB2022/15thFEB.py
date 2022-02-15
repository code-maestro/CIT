# 1. Create a program to replace the dice. When the program is run, it should roll the dice and output the result of each dice.
import random

def dice():

    player_one = random.randint(1, 6)
    player_two = random.randint(1, 6)

    print(f"Player One Dice : {player_one}")
    print(f"Player Two Dice : {player_two}")

    if player_one == player_two:
        print(f"It was a Draw {player_one}")
    elif player_one > player_two:
        print(f"Player one wins with: {player_one}")
    else:
        print(f"Player two wins with: {player_two}")

dice()

# 2.Create a while loop that prints your name 5 times in uppercase letters.
def name(name):
    i = 0
    while i < 5:
        print(name.upper())
        i += 1

name(input("Enter your name : "))

# 3.Create a pyramid pattern object using the number 1.
def pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print('1', end='')
        print()

pyramid(5)


