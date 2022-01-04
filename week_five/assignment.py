"""
TUESDAY ASSIGNMENT (Week 5)

"""

# class that prints out the names with number
class Names:
    def __init__(self, names):
        self.names = names

    def print_names(self):
        for i in range(len(self.names)):
            print(i+1, self.names[i])

    def print_names_with_number(self):
        for i in range(len(self.names)):
            print(i+1, self.names[i])

print(Names.print_names_with_number(Names(["John", "Paul", "George", "Ringo"])))

# function finds median, mode, mean and sum of the list
def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[int(len(numbers)/2)] + numbers[int(len(numbers)/2) - 1]) / 2
    else:
        return numbers[int(len(numbers)/2)]

print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 2 array of numbers and return the multiple of the two arrays
def multiply_arrays(array1, array2):
    result = []
    for i in range(len(array1)):
        result.append(array1[i] * array2[i])
    return result

print(multiply_arrays([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))