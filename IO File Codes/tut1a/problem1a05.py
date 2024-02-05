import numpy as np
import matplotlib.pyplot as plt
f1  = lambda x , t , k , w : 1*np.sin(k*x - w*t)
t = np.linspace(0,10, 100)
print(t)
w  = 2*np.pi*50
k = 2*np.pi/2
x = np.linspace(-10 , 10  , 4001)
for i in range(0 , len(t)):
    plt.clf()
    y = f1(x , t[i] , k , w)
    plt.xlim(-10 , 10 )
    plt.ylim(-1, 1 )
    plt.plot(x , y ,  color = 'blue' , label = f'time = {t[i]}')
    plt.legend()
    plt.pause(0.1)
plt.show()
    
