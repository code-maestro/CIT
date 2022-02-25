# import numpy as np

# a = np.array([[100,120,140,160],[180,200,220,240]])
# b = np.array([1,2,3,43,4,6,7,8,9],ndmin = 5)
# a = np.array([[1,2,3,4],[5,6,7,8]])
# b = np.array([[[[10,20,30,40],[50,60,60,80],[90,100,110,120],[130,140,150,160]]]])


# print(a.shape)
# print(a.reshape(4,2))
# print(a.reshape(1,8))
# print(b.shape)
# print(b.reshape(1,16))
# print(b.reshape(8,2))

# print(a.ravel())
# print(b.ravel())

# print(a.transpose())
# print(b.transpose())#Transform a row into a column(Transpose)

# print(a[0]*a[1])

# c = np.arange(1,10,2)
# print(c)

# d = np.arange(0,10,2)
# print(d)

# f = np.arange(20)
# print(f)



# g = np.arange(10)
#print(g)

# print(g.reshape(2,5))
# print(g.transpose())
# print(f.reshape(5,4))
# print(f.reshape(2,10))#First number is the row and second number is the column

# print(f[7:14])


# list1 = [23,4,55,67,8,8,99,95,3,3,2,22,2,33,4,45,56,332,2]

# list2 = [454546,677,67,7868,89,898,95,32,32,233,2,2,111,3]

# merge_list = list1 + list2

# arr_merge = np.array(merge_list)

# print(arr_merge)


# # # # # # # # # # # # # # # # # # # #
# ASSIGNMENT

# # 1.Create a function that transform an array from rows to columns.
import numpy as np

# def transform():
#     rows = np.array([[1,3,5,7], [2,4,6,8]])
#     print(f"ROWS : {rows} \n")

#     columns = rows.transpose()
#     print(f"COLUMNS : {columns} \n")

# transform()


# # 2.Create an array,using the if statement find out if the numbers of dimensions is correct.
# rows = np.array([[1,3,5,7], [2,4,6,8]])
# print(rows)
# print(rows.ndim)

# if(rows.ndim == 2):
#     print("Correct")
# else:
#     print("WRONG")


# 3.Convert a list into an array and add two brackets to that new array.
list = [2,4,6,8,10]
arr = np.array(list, ndmin = 2)

print(f" LIST : {list} \n TO \n ARRAY : {arr} \n")

# # 4.Create two 2-d arrays and multiply each of them.
# p = np.array([[1,3,5,7], [2,4,6,8]])
# n = np.array([[-1,-3,-5,-7], [-2,-4,-6,-8]])

# print(f"PRODUCT OF p : {p[0]*p[1]}\n")
# print(f"PRODUCT OF n : {n[0]*n[1]}\n")

# 5.Create a right side triange pattern using the dollar sign'$'
# spaces = 5
# while spaces >= 1:
#     print("$" * spaces, "$" * (spaces-1))
#     spaces -= 1

for i in range(5):
    for space in range(0, 5 - i):
        print(" ", end="")
    for j in range(i, 2 * i -1):
        print("* ", end="")
    print()