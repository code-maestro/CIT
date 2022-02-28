# PASSWORD AUTHENTICATION
def auth(password, password_repeat):
    if password != password_repeat:
        print("WRONG \n")
    else:
        print("CORRECT \n")

auth(input("Enter First Password : \n"), input("Enter the Second Password : \n"))

# # PHONEBOOK SEARCH
# contacts = {
#     "sal": [
#         +256345242434,
#         "saldj@gmail.com"
#     ],
#     "marcus": [
#         +25634500434,
#         "marcus@gmail.com"
#     ],
#     "aon": [
#         +2563451110434,
#         "aon@gmail.com"
#     ]
# }

# print(f"\n {contacts.keys()}")

# def search(name):
#     email = contacts.get(name)
    
#     if email in contacts.keys():
#         print(f"{name}'s Email is {email[1]} \n")
#     else:
#         print("NOT FOUND \n")

# search(input("ENTER A NAME TO SEARCH : \n"))

# # NESTING LIST
# colors = ["red", "blue", "green", "yellow", "orange", "purple"]
# cars = ["Ford", "Chevy", "Alpine", "Toyota", "Honda", "BMW"]

# for i in colors:
#     for j in cars:
#         print(i, j)


# # game
# from random import randint

# def game(user):
#     options = ["ROCK", "PAPER", "SCISSOR"]
#     computer = options[randint(0,2)]
#     print(f" COMPUTER PICKED : {computer} \n")

#     if user == computer:
#         print(" DRAW \n")
#     elif user == "ROCK" and computer == "PAPER" or user == "PAPER" and computer == "SCISSOR":
#         print("COMPUTER WINS \n")
#     else: 
#     # user == "PAPER" and computer == "ROCK" or user == "SCISSOR" and computer == "PAPER":
#         print(" YOU WIN ")
    
# game(input("ROCK, PAPPER, SCISSOR: "))

# 3 days out that list.
daysoftheweek = ["Monday","Tuesday","Wednesday","Thursday","Friday"] 
print(daysoftheweek[:3])