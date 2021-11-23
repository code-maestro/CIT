"""
x = 1

while x != 10:
    print(x)
    break


i = 0

while i == 1:
    print(i)
    if i >= 5:
        print('Breaking')
        
print('Finish')


y = 1

while y <= 5:
    print(y)
    y+=1
    if y ==2:
        print("Statement")
        continue


amount_of_money = 1


while amount_of_money != 10:
    #amount_of_money+=1
    print("I recieved " + "$" + str(amount_of_money) + "Dollars")
    break

b = 2

while b < 10:
    b+=1 #1
    if b%2 == 0:
        print(str(b) + " is even")
    else:
        print(str(b) + "is odd")
    
"""



sports_teams = {
    'Baseball':{
        'La':'Dodgers',
        'Ny':'Yankees',
        'Boston':'RedSox',
        'Ny':'Mets'},
    'Basketball':{
        'LA': 'Lakers',
        'Boston':'Celtics',
        'New York': 'Knicks',
        'Dallas':'Mavs'
        }
    }

"""
print(sports_teams)

for i in sports_teams.keys():
    print(i)

for i in sports_teams.values():
    print(i)
"""
for i,m in sports_teams.values():
    print(i)
    for x,y in m.items():
        print(x,y)
