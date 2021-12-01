

# Question one
def bubblesort(lst):
        # get the length of the list
        n = len(lst)
        # go through the list n number of times
        for i in range(n):
                # variable to keep check for any swaps
                swap = False
                # traverse through all adjacent elements
                for j in range(0, n-i-1):
                    # if current element greater than next element, swap them
                    if lst[j]>lst[j+1]:
                        lst[j], lst[j+1] = lst[j+1], lst[j]
                        swap = True
                # if no swaps, then break out of the loop
                if swap == False:
                        break
        # print the final sorted list
        print(lst)

# an example unsorted list 
y = [1,5,4,6,7,8,3,2,12,10,9,11]

# function call to sort list y
bubblesort(y)

#Question two

def selectionSort( data ):
    n = len(data)
    for i in range( n - 1 ):
        #define the minimum index
        minValue = i 

        #start from minvalue add one and go all the way till len
        for j in range( i + 1, n ):
            if data[j] < data[minValue] :
                minValue = j
                
        #if i element already contains minimum element dont swap it
        if minValue != i :
            temp = data[i]
            data[i] = data[minValue]
            data[minValue] = temp

    return data

arr = [10,4,3,9,8,2,5,6]
print(selectionSort(arr))


#Question three

first = ["Black","Yellow","Red"]
second = ["Harrier","Toyota","Corona"]
final = []
for i in first:
    for j in second:
        final.append(i+j)
print(final)
