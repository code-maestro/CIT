# # ASSIGNMENT FOR 3rd JANUARY 2022
# # 1. Create a file with 2022's goals
# f= open("michael_2022_goals.txt","w+")
# f.write("1. Become a better software developer\n")
# f.write("2. Exercise and get in shape\n")
# f.write("3. Become a data scientist and ML engineer\n")
# f.write("3. Binge more Formula one\n")
# f.close()

# # 2. Create a lambda function wuth 3 arguments
# names = lambda x,y,z: x+y+z
# print(names("Michael ","Schumacker ","Mick"))

# # # 3. Create a function that accepts user input
# # champ = lambda z: z
# # print(champ(input("Who is your favorite champion? ")))

# # 4. Create a while loop that prints 1-30 but skips 25
# i = 0
# while i <= 30:
#     if i == 25:
#         i += 1
#     else:
#         print(i)
        # i += 1

# 5. Create a function that prints random numbers with 2 arguments
# import random as rand
# def random_numbers(x,y):
#     for _ in range(x,y):
#         print (rand.randint(x,y))

# random_numbers(1,10)

import random
def random_numbers(x,y):
    print (random.randint(x,y))

random_numbers(1,10)