# # 1. Create a 2-D array and using a funtion print out the number of dimension of that array.
# import numpy as np
# a = np.array([[1, 44, 12], [23, 322, 32]])
# print(a.shape)
# print(a.ndim)

# # 2. You need to make a program that counts the number of vowels in a given text. The vowels are a,e,i,o,u. Take a string as input and output the number of vowels.
text = input("Enter a random string : ")
vowels = ["a", "e", "i", "o", "u"]
number_of_vowels = 0
for i in text:
    if i in vowels:
        print(i)
        number_of_vowels += 1
        
print(f"The Number of vowels in the string {text} are {number_of_vowels}")

# # 3.Create a upside down pyamid object pattern using binary numbers "1,0".

# spaces = 0

# while spaces < 5:
#     print("*" * spaces)

#     for j in range(2*spaces-1):
#         print('1', end='')
    
#     spaces += 1

#     # while binary_numbers  0:
#     #     print("1" * binary_numbers)

#     # binary_numbers -= 1
#     # 
