import matplotlib.pyplot as plt
import math as math

'''
METR-1003 Homework 2 Quesiton 3
@author William McGovern-Fagg
@author wrmf
'''

counter = 200
vapour = []
temp = []

while(counter <= 400):
    vapour.append(math.pow(6.11, (((2.5*pow(10, 6))/461)*((1/273.15)-(1/counter)))))
    temp.append(counter)
    counter += 1

plt.plot(temp, vapour)
plt.ylabel("Saturation Vapour Pressure hPa")
plt.xlabel("Temperature in K")
plt.savefig("plt.png")