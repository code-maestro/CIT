# ASSIGNMENT
from multiprocessing.reduction import duplicate
import numpy as np
import matplotlib.pyplot as plt

# # 1.Create a list called fruits and show us which fruit has the most sales using matplotlib.
# plt.style.use('dark_background')

# fruits = ['apple', 'peach', 'pineapple', 'watermelon']
# sales = np.random.randint(5, 25, size=(4))
# plt.title('FRUIT SALES')
# plt.bar(fruits, sales)
# plt.show()

# 2.Create 4-D array then reshape it.
arr = np.array([[[[23, 22], [12, 11]]]])
print(arr.ndim)
print(arr.reshape(2, 2))

# 3.Create a list of numbers and find out how many duplicate values is in your list.
# duplicate = [4, 12, 40, 22, 4, 12]

# 4.Create 2 arrays and divide both of them.
one = np.array([4, 12, 40, 22])
two = np.array([2, 3, 4, 4])
print(one/two)
