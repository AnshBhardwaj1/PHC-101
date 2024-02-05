import numpy as np
import matplotlib.pyplot as plt
g = 9.81
f1 = lambda v , the , t : (v)*np.cos(the) *t
f2 = lambda v , the , t : v*np.sin(the) - (1/2)*g*t**2
v_0 = 20
theta = np.pi/6
t = np.arange(0 , 4 , 0.1)
x1 = f1(v_0 , theta , t)
y1 = f2(v_0 , theta , t)
for i in range(0, len(t)):
    plt.clf()
    plt.xlim( 0,100)
    plt.ylim( -100,100)
    
    
    plt.plot(x1[:i + 1] , y1[: i + 1] , '^',  label = f'{t[i]}' , markersize = 3, color = 'blue')
    plt.legend()
    plt.pause(0.01)
plt.show()
