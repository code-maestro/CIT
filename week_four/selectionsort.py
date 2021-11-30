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