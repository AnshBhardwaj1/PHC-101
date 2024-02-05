import numpy as np
import matplotlib.pyplot as plt
xint = np.array([0,100,200,300,400,500,600,700,800,900,1000])
yint = np.array([0,300 ,380 , 340 , 230, 240 , 320 , 375 , 345 ,110 ,0 ])
def interpol(x , xint = xint    , yint = yint  ):
    sum = 0
    for i in range(len(xint)):
        p = yint[i]
        for k in range(len(xint)):
            if k == i :
                continue
            p *= (x - xint[k])/(xint[i] - xint[k])
        sum += p
    return sum

z = np.array([0 ,(1/3)* np.sqrt(5 - 2*np.sqrt(10/7)) , (-1/3)* np.sqrt(5 - 2*np.sqrt(10/7)) , (1/3)* np.sqrt(5 +  2*np.sqrt(10/7)) , (-1/3)* np.sqrt(5 +  2*np.sqrt(10/7))])
w = np.array([128/255 , (322 + 13*np.sqrt(70))/900 , (322 + 13*np.sqrt(70))/900 ,(322 - 13*np.sqrt(70))/900 ,(322 - 13*np.sqrt(70))/900 ])
def gauss_quad(a , b , f ):
    ans =( (b-a)/2 )*w * f( ((b-a )/2)*z + (b+a)/2)
    return sum(ans)
def simpson( x , y ):
    h = x[1] - x[0]
    sum = y[0] + y[-1]
    n = len(y)
    for i in range(1 , n ):
        sum += (i%2 + 1 )*2*y[i]
    return sum*h/3
print(simpson(xint , yint))
print(gauss_quad(0 , 1000 , interpol ) )

