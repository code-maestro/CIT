print(3 != 4)
print(4 == 5)
print(6 > 7)
print(6 < 7)

#And operator both condition need to be correct

a= 5
b = 6

print(a == 4 and b == 6)
print(a >= 5 and b <= 6)
print(a != b and b == 6)


#The or operator only one condition needs to be true


print(a != 5 or b == 6)
print(a < 2 or b > 7)
print(a < b or 9 > 8)


if a > b:
    print("True")
elif a == b:
    print("Could be True")
else:
    print("False")


def my_func(c):
    if c == 20:
        return True
    elif c == 30:
        return True
    else:
        return False

print(my_func(30))


#in operator is when a certian value is in a list,dictionary,ect.


list1 = ["Monday","Tuesday","Wednesday","Thurday","Friday"]


print("Monday" in list1)
print("Saturday" in list1)

print("Tuesday" in list1)
print("friday" in list1)


print("Monday" not in list1)
print("Sunday" not in list1)


if "Sunday" in list1:
    print("Yes it is")
elif "Sunday" not in list1:
    print("I guess its not!")
else:
    print("End of statement")
    

    if ("Winter" not in tup1 and "Winters" in tup1) or ("Jack" in tup1):
    print("True")
elif ("Summer" in tup1) or ("Summers" in tup1):
    print("True statement")
else:
    print("False")

# https://1drv.ms/p/s!AgYEaoh811UQgRKVGGu0vyw8_HRN?e=xe3CF9
