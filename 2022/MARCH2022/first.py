
# import matplotlib.pyplot as plt

# plt.style.use("dark_background")

# arr2 = [20,2,50,36,17,90,42,36,1,9]
# arr3 = np.arange(0,10,1)

# def selectionsort(num): 
#     for i in range(len(num)):
#         midindex = i #splitting list into 2
#         for j in range(i+1,len(num)):
#             plt.bar(arr3,arr2)#Visualizing of the graph
#             plt.pause(0.01)#Duration time
#             plt.clf()
#             if arr2[j] < arr2[midindex]:#Trying to find the number that is the least valued to place in the ordered list
#                 midindex = j
#         arr2[i],arr2[midindex] = arr2[midindex],arr2[i]#Swap happens

# selectionsort(arr2)
# plt.show()



# allstar_players = [29,32,27,33,36,24,22,20]

# def percentage_pts(args):
#     args1 = np.percentile(allstar_players,2)
#     return args + str(args1)
# print(percentage_pts("The percentile is: "))

# ASSIGNMENT
from random import randint
import numpy as np

# 1.50 percent of the class failed the exam, create a list of student scores that score under a 70.
def scores():
    pass_mark = 70
    students = 20
    marks = []
    while students > 0:
        marks.append(randint(0, 99))
        students -= 1

    print(marks, "\n")
    print("\n", np.percentile(marks,2), "\n")

    if np.percentile(marks,2) == 50:
        for i in marks:
            if i < pass_mark:
                print(i)
            i += 1

scores()

# # 2.Create a 6-D array and transform it to all rows.
# six = np.array([[[[[[1, 2], [3,4], [5, 6], [7,8], [9,10], [11,12]]]]]])
# # a = np.arange(64).reshape(8, 2)
# # print(a)
# print(six.ndim)
# print(np.vstack(six))

# # 3.Create a 8-D array and reshape the array.
# eight = np.array([[[[[[[[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]]]]]]]])
# print(eight.ndim)
# print(eight.reshape(4, 6))

# # 4.Create a x array and y array and multiple it than reshape the new array.
# x = np.array([2,4,6,8])
# y = np.array([1,3,5,7])
# new_array = x * y

# print(new_array.reshape(2,2))

# z = np.hstack(x)
# w = np.vstack(x)
# m = np.hstack((x,y))
# mv = np.vstack((x,y))


# print("x axis array:")
# print(x)
# print("y axis array:")
# print(y)
# print("Horizontal Stack array: ")
# print(z)
# print("Vertical Stack array: ")
# print(w)
# print("Merging x axis and y axis Horizonally:")
# print(m)
# print("Merging x axis and y axis Vertically:")
# print(mv)
# print(mv.shape)
# print(mv.reshape(4,5))
# print(m.reshape(2,10))