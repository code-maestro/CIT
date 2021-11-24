
"""

    AJUNA MICHAEL'S WEDNESDAY (Week Three) ASSIGNMENT

"""

# 1.Create a dictionary called "Report Card" the keys will be the name of the students and the values will be their grades.
report_card = {
    "marina": "C",
    "jeddah": "B",
    "silverstone": "D",
    "zandvort": "D",
    "Sam": "B+",
    "Sally": "F",
    "Sue": "A"
    }

print(report_card)

# 2.In your report card dictionary change one of the students grades.
report_card["jeddah"] = "A"

print(report_card["jeddah"])

# 3.Create a while loop that prints 10 numbers but it skips the number 3.
i = 0
while i < 10:
    i+=1
    if i == 3:
        continue
    print(i)

# 4.Create a list that prints out all the items outside the list.
list = [1,2,3,4,5]
print(list[-6:0])

# 5.Create a if statement that use the input method.
if input("Enter a good driver ") == "Lewis":
    print("Lewis is a good driver")
else:
    print("Try again")
