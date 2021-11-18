import random

y = "COMPUTERCLASS"

print(y[8:11])
print(y.index('S'))
print(y.count('A'))
print(y.count('S'))
print(y.lower())

def sum_of(num1):
    a = random.randint(1,20)
    print(a)
    return (a*num1)

print(sum_of(4))
