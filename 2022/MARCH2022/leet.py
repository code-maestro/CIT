
# words = ["cat","bt","hat","tree"]
# chars = "atach"
# i = 0
# number = 0
# while i <= 3:
#     print(words[i])

#     c = ""
#     for words[i] in chars:
#         print(words[i])

#     # for chars in words[i]:
#     #     print(chars)
#     # for c in chars:
#     #     # print(words[i].count(c))
#     #     number += words[i].count(c)
        
#     i += 1

# print(number)

import numpy as np

a = np.arange(0,10,1).reshape(2, 5)
print(a)

# def average_median(list):
#     return print(" Average = ", sum(list)/12, "\n Median = ", np.median(list))

# list = [2, 4, 6, 8, 10, 11, 14, 16, 17, 20, 22, 44]
# average_median(list)



# arr =   np.array([[23, 9],[23, 9],[23, 9],[23, 9],[23, 9],[23, 9],
#             [21, 20],[3, 10],[3, 99],[101, 12],[21, 29],[25, 69],
#             [273, 159],[231, 9],[223, 89],[223, 29],[123, 59],[78 ,19],
#             [221, 29],[200, 109],[123, 59],[65, 39],[213, 39],[25, 15],
#             [237, 99],[213, 129],[13, 149],[44, 49],[203, 49],[26, 29],
#             [283, 79],[133, 309],[21, 109],[20, 69],[233, 39],[27, 90]])

# arr.reshape(4, 9)

# old_array = np.arange(1,37,1).reshape(6,6)
# print(old_array)
# new_array = old_array.reshape(4, 9)
# print(new_array)

# arr = np.random.randint(23, 100, size=(20))
# print(arr)
# greater = []

# for i in arr:
#     if i <= 55:
#         greater.append(i)
# print("\n", greater , " == " , len(greater))

