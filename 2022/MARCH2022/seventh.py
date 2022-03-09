import numpy as np
import matplotlib.pyplot as plt

# # 1.Create a 2-D array and grab 3 numbers in the second column.
# arr2d =  [[2, 4, 6, 8], [10, 12, 14, 16]]
# print(arr2d[1][:3])


# # 2.Create a list called company_data, using a funtion the company needs to know the total average,the variance, and how spread out the data is.
# company_data = np.arange(20,100,2)

# def calculations(list):
#     spread = np.std(list)
#     variance = np.var(list)
#     average = np.average(list)
    
#     return("AVERAGE : ", average , "V : ", variance , "Spread out : ", spread)
    
# print(calculations(company_data))


# # 3.Create 2 arrays showing the x axis from 20 to 100 and the y axis from 120 to 200 (use matplotlib to visualize the array for x and y).
# x = np.array(np.arange(20,100))
# y = np.array(np.arange(120,200))

# plt.scatter(x,y)
# plt.show()



# # 4.Create a 2-d array and multiple both columns then reshape the new array.
# two = np.arange(0,12,1).reshape(2, 6)
# print(" OLD 2D ARRAY : \n" , two)
# new = np.multiply(two[0], two[1]).reshape(3, 2)
# print("\n NEW ARRAY \n", new)


# # 5.Create any  sorting algorithm and show us the animation using matplotlib.
# # BUBBLE SORT
# arr = [90,-22,70,17,-8,-37,10,-2,55,9]
# arr2 = np.arange(0,10,1)
# print(arr2)

# def sort():
#     n = len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             plt.bar(arr2,arr)
#             plt.pause(0.01)
#             plt.clf()
#             if arr[j] > arr[j+1]:
#                 arr[j+1],arr[j] = arr[j],arr[j+1] #Swapping

# sort()
# plt.show()

#5.
arr3 = [90,22,70,17,8,37,10,2,55,9]

arr4 = np.arange(0,10,1)

def selectionsort(num):
    for i in range(len(num)):
        midindex = i
        for j in range(i+1,len(num)):
            plt.bar(arr4,arr3)
            plt.pause(0.05)
            plt.clf()
            if arr3[j] < arr3[midindex]:
                midindex = j
        arr3[i],arr3[midindex] = arr3[midindex],arr3[i]

selectionsort(arr3)
plt.show()
