import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

x = np.array([5,10,15,20,25,30])
y = np.array([10,20,30,40,50,60])

#         row,columns,index
plt.subplot(2,3,1)
plt.bar(x,y)
plt.title('Bar Graph')


x1 = np.array([66,70,80,100,30,40])
y1 = np.array([1,10,20,80,7,15])

plt.subplot(2,3,2)
plt.plot(x1,y1)
plt.title('Plot Graph')


y2 = np.array([10,21,3,40])

sports_teams = ["Lakers","Yankees","Rangers","Giants"]
c2 = ["yellow","grey","red","blue"]


plt.subplot(2,3,3)
plt.pie(y2,labels=sports_teams,colors = c2,autopct='%1.1f%%')
plt.legend('Teams')
plt.title('Pie Chart')

x3 = np.arange(1,10,1)
y3 = np.arange(10,100,10)


plt.subplot(2,3,4)
plt.scatter(x3,y3)
plt.title('Scatter Plot')


x4 = np.arange(10,100,10)
y4 = np.arange(100,1000,100)

plt.subplot(2,3,5)
plt.plot(x4,y4)
plt.grid()
plt.title('Grid Graph')


x5 = np.arange(1,10,1)
y5 = np.arange(10,100,10)


plt.subplot(2,3,6)
plt.bar(x5,y5)
plt.title('Bar Graph 2')


plt.suptitle('Multiple Graphs Diagram')
plt.show()

# Homework assignment

# 1.Create a grid graph called Vaccine Data, and display 

# in the graph of the data increasing then decreasing at the end.

# 2.Create a 4-D array and change it to a 1-D array.

# 3.Create 4 different Graphs in 1 figure.

# 4.Find out the standard Deviation for the Vaccine Data.
