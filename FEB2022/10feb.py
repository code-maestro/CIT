# THURSDAY, 10TH FEBUARY 2022 ASSIGNMENT
# MICHAEL AJUNA

# 1. Create a function to find the equation of 3 times 8 to the power of 3.
def fun():
    return 3*8**3

print(fun())


# 2. Create a list called students_scores and find the total average for student scores.
student_scores = [80, 86, 56, 100]

print("The Average of Student scores: ", sum(student_scores)/len(student_scores))


# 3.Create a class called Square_root to find the square root of a number.
class Square_root:
    def square_root(self, number):
        self.number = number
        return self.number**0.5

number = Square_root()
print(number.square_root(9))


# 4.Reversing a string is a common task during coding interviews, Given a string as input, output the string in reverse.
def reverse(string):
    return string[::-1]

reverse(input("Enter any string : "))