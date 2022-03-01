import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")

arr2 = [20,2,50,36,17,90,42,36,1,9]
arr3 = np.arange(0,10,1)

def selectionsort(num): 
    for i in range(len(num)):
        midindex = i #splitting list into 2
        for j in range(i+1,len(num)):
            plt.bar(arr3,arr2)#Visualizing of the graph
            plt.pause(0.01)#Duration time
            plt.clf()
            if arr2[j] < arr2[midindex]:#Trying to find the number that is the least valued to place in the ordered list
                midindex = j
        arr2[i],arr2[midindex] = arr2[midindex],arr2[i]#Swap happens

selectionsort(arr2)
plt.show()
