import numpy as np
n = int(input("Enter order : "))
a = np.random.randn(n, n)
print("Initial Matrix : ", a)
print("Final Matrix : ", a.T )
