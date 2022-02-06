def bubbleSort(array):
    """Use swapped variable to keep track of swapping
    Best Case ==> O(n) Iterates arr once if sorted
    Worst Case ==> 0(n^2)
    """
    iterations = 0
    for i in range(len(array)):
        print(f"Bubble sort {iterations} iterations: {array}")
        # keep track of swapping
        swapped = False
        
        # loop to compare array elements
        for j in range(0, len(array) - i - 1):
            # compare two adjacent elements
            # Sort in Ascending order
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping occurs if elements
                # are not in the intended order
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        iterations += 1
        # no swapping means the array is already sorted
        # so no need for further comparison
        if not swapped:
            break

data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)

# WITH THE WHILE LOOP
def bubbleSort3(arr):
    '''Using while and for loops
    Best Case ==> O(n) Iterates arr once if sorted
    Worst Case ==> 0(n^2)
    '''
    swap = True
    iterations = 0
    comparisons = 0
    while swap:
        print(f"Bubble sort {iterations} iterations: {arr}")
        comparisons += 1
        swap = False
        for num in range(len(arr) - 1):
            comparisons += 1
            if arr[num] > arr[num + 1]:
                # swap elements
                swap = True
                arr[num], arr[num + 1] = arr[num + 1], arr[num]
        iterations += 1

data = [-2, 33, 0, 11, -9]

bubbleSort3(data)

print('Sorted Array in Ascending Order:')
print(data)