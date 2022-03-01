# no 1
arr = [23, -2, 33, -4, 12, 0]

def bubblesort(arr):
    while True:
        swap = False
        n = len(arr)
        for i in range(0,n -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]

                swap = True
        if not swap:
            return arr
print(bubblesort(arr))

# no. 2
import numpy as np
arr1 = np.array([[[1,2,3,4,5],[6,7,8,9,5],[6,7,8,9,10]]])

def ndmin_values(n):
    x = np.ndim(arr1)
    return n + str(x)

print(ndmin_values("Dimension: "))

# no.3 
arr2 = np.array([[[[[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]]]]])
print(np.ndim(arr2))

def shapeof_array():
    print(arr2.reshape(2,6)) #Reshape to a 2-D array
shapeof_array()

# no.4
for i in range(5):
    print("Dashawn")

# no.5
print(tuple(arr))