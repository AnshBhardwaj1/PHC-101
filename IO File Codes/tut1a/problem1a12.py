import numpy as np
import matplotlib.pyplot as plt
T0  = 100
Tl = 20
a = 0.01
k  = 200
s = 1
d = 1
t = [0]
temp = [T0]
while temp[-1] > Tl + 1 :
    t.append(0.1 + t[-1])
    temp.append(temp[-1]  -  0.1*(k*a*(temp[-1] - Tl))/(s*d))
plt.plot(t , temp , label = 'Temperature ' )
plt.legend()
plt.show()


