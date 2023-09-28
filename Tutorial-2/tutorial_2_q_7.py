import numpy as np

def f(x, h, v):
    f = np.sin(x) - ((2*9.8*h)**0.5)/v
    return f
def df(x):
    df = np.cos(x)
    return df

v = float(input("v0 : "))
h = float(input("h : "))
x = np.pi/6

for i in range(1000):
    intercept = x - (f(x, h, v)/df(x))
    x = intercept

print("alpha : ", x)
