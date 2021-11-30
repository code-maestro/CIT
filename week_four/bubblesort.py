arr = []

numbers = int(input("Enter random numbers : " ))

for i in range(numbers):
    if len(arr) < 5:
        arr.append(int(input("Enter number : ")))

def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array


print(bubblesort(arr))