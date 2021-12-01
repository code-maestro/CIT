arr1 = [100,49,2,1,34,-5,36,72]

def selectionsort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1,len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return print(array)

selectionsort(arr1)


# Selection sort in Python
def selectionSort(array):
    iterations = 1
    size = len(array)
    for step in range(size):
        print(f"Selection sort {iterations} iterations: {array}")
        min_idx = step
        for i in range(step + 1, size):
            # Sorting in Ascending order
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        iterations += 1
        array[step], array[min_idx] = array[min_idx], array[step]

data = [-2, 5, 0, 11, -9]

selectionSort(data)

print('Sorted Array in Ascending Order:')
print(data)