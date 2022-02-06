fruits = ["Apples","Peaches","Oranges","Bananas"]

colors = ["Red","Yellow","Black","Purple","Purple"]

#Removes the element at the specified position​
fruits.pop(2)

print(fruits)

#Removes the item with the specified value
fruits.remove("Bananas")
print(fruits)

#Insert a new item inside our list

fruits.insert(1,"Oranges")

print(fruits)

#Extend method extends our list
fruits.extend(colors)

print(fruits)

#Reverse our list
fruits.reverse()
print(fruits)



#Sorts our list
fruits.sort()
print(fruits)


x = fruits.count("Red")

print(x)
