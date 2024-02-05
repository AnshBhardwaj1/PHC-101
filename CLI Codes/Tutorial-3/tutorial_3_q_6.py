import numpy as np
import math
import matplotlib.pyplot as plt
def fact(x):
    f = math.factorial(x)
    return f

def H(n, x):
    h = 0
    p = int((n-1)/2)
    if(n%2 == 0):
        p = int(n/2)
    for s in range(p+1):
        h += (-1)**s*(2*x)**(n-2*s)*fact(n)/(fact(n-2*s)*fact(s))
    return h
n = int(input("Enter n in range [1,3] : "))
x = np.linspace(-5, 5, 1000) #I_array = [I(theta, d, lambd, I0) for theta in theta_array]
y = [H(n, xValue) for xValue in x]

plt.plot(x, y)
plt.xlabel("x for n = "+ str(n))
plt.ylabel("H(x)")
plt.show()

