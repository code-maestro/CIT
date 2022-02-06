
# Global list
thelist =  [12, -3, 5, 23, 30, -32]

# # Using the bubblesort method create another way to sort a unsorted list.
# def bubblesort(mylist):
#     for i in range(len(mylist)):
#         for j in range(0, len(mylist)-i-1):
#             if mylist[j] > mylist[j+1]:
#                 # swap
#                 mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
#     return mylist

# print(bubblesort(thelist))


# Using the Selectionsort method create another way to sort a unsorted list
def selectionsort(mylist):
    loops = 0
    for i in range(len(mylist)):
        print(" LOOP : " , loops , " LIST : " , mylist )
        smallest = i
        for j in range(i + 1, len(mylist)):
            if mylist[smallest] > mylist[j]:
                smallest = j
        mylist[i], mylist[smallest] = mylist[smallest], mylist[i]

    loops += 1

    return mylist

print(selectionsort(thelist))

# # Create a nesting loop that prints two list. Colors and Cars
# colors = ["red", "blue", "green", "yellow", "orange", "purple"]
# cars = ["Ford", "Chevy", "Alpine", "Toyota", "Honda", "BMW"]

# for i in colors:
#     for j in cars:
#         print(i, j)
