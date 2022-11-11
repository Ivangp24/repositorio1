
import pandas as pd
import matplotlib.pyplot as plt

z1 = ['BMW', 200000]
z2 = ['MERCEDES', 500000]
z3 = ['AUDI', 300000]
z4 = ['OPEL', 100000]
z5 = ['MUSTANG', 700000]

listcars = [z1, z2, z3, z4, z5]

cars = pd.DataFrame(listcars, columns=['marca', 'ventas'])

print(cars)

plt.plot(cars['marca'], cars['ventas'])
plt.show()

plt.scatter(cars['marca'], cars['ventas'])
plt.show()

plt.barh(cars['marca'], cars['ventas'])
plt.show()

plt.bar(cars['marca'], cars['ventas'])
plt.show()

plt.pie(cars['marca'], cars['ventas'])
plt.show()


