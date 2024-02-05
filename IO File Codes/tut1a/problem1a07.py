import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-4 , 4.1 , 0.1)
print(len(x))
def y1(x , theta1, n1 , n2 ):
    if x <= 0:
        return (4 - (np.tan(theta1)*(x + 4 )))
    else :
        return (4*(1-np.tan(theta1))) - (n1)*(np.sin(theta1))*(x)/(np.sqrt(n2**2 - (n1**2)*np.sin(theta1)**2))
y = np.array([])
theta1 = float(input('Enter value of theta: '))
n1 = 1.5
n2 = 1
for i in range(len(x)):
    plt.ylim(-5,5)
    plt.axvline(0 , label = 'Medium Boundaries')
    y = np.append(y , y1(x[i] , theta1  , n1 , n2 ))
    plt.plot(x[:i + 1 ] , y , '^',color = 'blue' , markersize = 2)
    plt.pause(0.01)
plt.show()
