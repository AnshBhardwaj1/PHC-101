import numpy as np
def omega(s, t):
    def f(x, s, t):
        f = s - (9.8/2*x**2)*((np.exp(x*t) - np.exp(-x*t))/2 - np.sin(x*t))
        return f
    x0 = np.pi/4
    x1 = np.pi/2

    for intercept in range(1, 10):
        fx0 = f(x0, s, t)
        fx1 = f(x1, s, t)
        xi = x0 - (fx0 / ((fx0 - fx1) / (x0 - x1)))
        x0 = x1
        x1 = xi

    print("The root is at : ", xi)    

s = float(input("Enter s : "))
t = float(input("Enter t : "))

omega(s, t)