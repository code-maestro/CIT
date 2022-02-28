import numpy as np
import matplotlib.pyplot as plt


plt.style.use("dark_background")

arr = [90,22,70,17,8,37,10,2,55,9]

arr2 = np.arange(0,10,1)

print(arr2)

def sort_algorithm():
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            plt.bar(arr2,arr)
            plt.pause(0.01)
            plt.clf()
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1] #Swapping


sort_algorithm()
plt.show()
