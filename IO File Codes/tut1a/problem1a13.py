import numpy as np
import matplotlib.pyplot as plt
n01 = 1000
n02 = 500
lam1 = 0.01
lam2 = 0.02
def func(n0 , lam , t ):
    return n0*np.exp(-lam*t)
t = np.arange(0,25 , 1)
n1 = func(n01 , lam1 , t )
n2 = func(n02 , lam2 , t )

fig = plt.figure()
plt.subplot(1,2,1)
for i in range(len(t)):
    plt.clf()
    plt.plot(t[ : i+1] , n1[ :i+1] , '^' , color = 'blue')
    plt.pause(0.01)
plt.subplot(1,2,2)
for i in range(len(t)):
    plt.clf()
    plt.plot(t[ :i+1] , n2[:i+1] , color = 'red')
    plt.pause(0.01)
plt.show()



