import numpy as np
 
def trapezoidal(a, b, N, func):
    
    def f(x):
        f = eval(func)
        return f
    
    x = np.linspace(a, b, N)
    y = f(x)
    f = 0.0

    for k in range(len(x) - 1):
        f += 0.5 * ((x[k+1] - x[k])*(y[k+1] + y[k]))
    print(f)



a = float(input("a : "))
b = float(input("b : "))
N = int(input("N : "))
func = input("f(x) : ")

trapezoidal(a, b, N ,func)