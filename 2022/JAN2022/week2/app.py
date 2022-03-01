# Write a program to take a number as input, 
# and output a list of all the numbers below that number, 
# that are a multiple of both 2 and 6. 
# This is the question in the pre test someone here talked about

# mylost = [ x for x in range(1,100) if x %2 == 0 and x % 6 == 0]

# print(mylost)

# # printing stars from the right
# for i in range(10):
#     print(i * '*')

# stars from the left
for i in range(5): 
    for j in range(5-i-1):
        print(" ", end="")
    for x in range(i+1):
        print("*", end="")
    print("")

# # simpler version of stars from the right
# for i in range(5):
#     print(" " * (5-i-1) + "*" * (i+1))

# # stars from the left with a space
# for i in range(5): 
#     for j in range(5-i-1, 0, 5+i-1):
#         print(" ", end="")
#     for x in range(i+1):
#         print("*", end="")
#     print("")