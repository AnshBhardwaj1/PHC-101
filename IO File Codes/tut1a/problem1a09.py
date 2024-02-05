import numpy as np
import matplotlib.pyplot as plt
g = 9.81
l = 3
def ode2(x0 , y1 , y2 , f1 , f2 , xn , n):
  h = (xn - x0 )/(n)
  x =  np.arange(x0 , xn + h, h)
  y1 = [y1]
  y2 = [y2]
  for i in range(n):
    y1.append(y1[-1] + h*f1(x[i] , y1[-1] , y2[-1]))
    y2.append(y2[-1] + h*f2(x[i] , y1[-1] , y2[-1]))
  return x , y1 , y2
f1 = lambda t ,  theta , w  : w
f2 = lambda  t , theta , w  : (-1)*g*(np.sin(theta))/l


t , theta , w = ode2(0 , 1, 0,f1 , f2 , 20 , 1000)
x = l*(np.sin(theta))
for i in range(len(t)):
    plt.xlim(0,30)
    plt.ylim(-5,5)
    plt.plot(t[:i+1],theta[:i+1] , label = 'Theta')
    plt.plot(t[:i+1],w[:i+1] , label = 'Omega')

    plt.plot(t[:i+1] , x[:i + 1] , label = 'x')
    plt.legend()
    plt.pause(0.00001)
    plt.clf()
plt.show()
