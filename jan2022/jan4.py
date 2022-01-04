
# AJUNA MICHAEL JANUARY 4TH 2022 ASSIGNMENT

# 1. Function that tales a string and a letter as arguments ans returns the count of the letter in the string
def count_letter(string,letter):
    letterCount = string.count(letter)
    return letterCount

print(count_letter(input(" ENTER ANY STRING :"), input("ENTER ANY LETTER :")))

# 2. Create a list of uppercase letters and change them to lowercase letters
worten = ["VETTEL", "HAMILTON", "VERSTAPPEN"]
for i in range(len(worten)):
    print(worten[i].lower())

# 3. A While loop that prints the odd numbers 1-15 but skips 5
i = 0
while i <= 15:
    if i % 2 != 0:
        if i != 5:
            print(i)
    i += 1

# 4. Create a turple and convert to a list
turple = ("KAMPALA", "IS", "HOT")
list = list(turple)
print(list)