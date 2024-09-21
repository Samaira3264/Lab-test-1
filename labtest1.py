import numpy as np
import matplotlib.pyplot as plt

x = np.array(['med1','med2','med3','med4'])

y = np.array([75,100,225,55])

z = np.array([25,45,30,10])

#stock = np.array([x][y][z])
#print[stock]

def add_med():
    newmed = (input("enter new medicine to the stock: "))

add_med()

def update_quan():
    for i in y:
        new_quant = int(input("enter new quantity of med"))
        y[i] = new_quant


sales = np.dot((75,100,225,55),(25,45,30,10))
profit = 0.2*sales
print("total sales if all items are sold= ",sales)

print("Current Inventory: ")
print(x)
print(y)
print(z)


plt.scatter(sales,profit)   
plt.show()

