import numpy as np
import matplotlib.pyplot as plt
fun = lambda A , w ,t : A*np.cos(w*t)
t = np.linspace(0,1,100)
A = 0.1
w = 2*np.pi
x = fun(A, w ,t)

for i in range(len(t)):
    plt.clf()
    plt.ylim(0)
    plt.xlim(-0.1,0.1)
    plt.plot(x[i] ,np.array([0]),'bs' , ms = 10)
    plt.pause(0.1)
plt.show()
