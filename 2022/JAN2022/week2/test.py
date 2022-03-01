#1.
tup = 1,2,3,4,5,6,7,8

x = 0

while len(tup) != x:
    print(tup[x])
    x+=1
    
        
#2.

list1 = [i for i in range(10)if i % 2 == 1]

        
print(list1)


#3.


school_periods = ["1st Periods","2nd Period","3rd Period","4th Period"]

school_subjects = ["Math","Science","History","Reading"]


for i in school_periods:
    for j in school_subjects:
        print(i.upper() + ":",j.lower())


#4.

user = int(input("Enter a number: "))


while user < 10:
    if user % 2 == 0:
        print(str(user) + " This is a even number")
    elif user  % 2 != 0:
        print(str(user) + " This is a odd number")
    else:
        ("Done")
    user+=1
print("Done!")


#5.

school_periods.extend(school_subjects)

print(school_periods)

for i in school_periods:
    print(i)
