import numpy as np
from scipy.integrate import trapz, simps, fixed_quad

def f(x):
    return -1/3 * x**2 + 2 * x

a = 0
b = 1
n = 20
x = np.linspace(a, b, n+1)
y = f(x)

result_trapezoidal = trapz(y, x)
result_simpson = simps(y, x)
result_gauss = fixed_quad(f, a, b, n=5)[0]

print("Trapezoidal rule:", result_trapezoidal)
print("Simpson's rule:", result_simpson)
print("5-point Gauss quadrature:", result_gauss)
