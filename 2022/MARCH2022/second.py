# ASSIGMENT
# 1.Create a 2-D array and slice out the second number in the second column.
two = [[44, 1], [30, 23]]
print("\n", two[1][1])

# 2. Create a list of numbers and find out the median value in that list using a function.
import numpy as np
def func(list):
    return(np.median(list))

print("\n", func([44, 1, 30, 23]))


# 3. Create an array with 20 random numbers and find out how many numbers is greater than,less than, or equal to 55.
arr = np.random.randint(23, 100, size=(20))
print("\n", arr)

i = 0

greater = []
smaller = []
equalto = []

for i in arr: 
    if i <= 55:
        greater.append(i)
    if i >= 55:
        smaller.append(i)

print("\n", greater , " == " , len(greater))
print("\n", smaller , " == " , len(smaller), "\n")
