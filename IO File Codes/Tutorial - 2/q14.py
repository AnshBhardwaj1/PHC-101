import numpy as np
from timeit import Timer
fint = open('input2014' , 'r')

cont = fint.readlines()
for i in range(len(cont)):
    cont[i] = eval(cont[i].strip())
z = np.array(cont[0])
w = np.array(cont[1])
def gaussian_quad(a , b , f ):
    ans = ((b-a)/2)*w*f(((b-a)/2)*z + (b+a)/2)
    return sum(ans)
print(gaussian_quad(0 ,2, lambda x : x**3 ))
c = lambda  : gaussian_quad(0 , 2 , lambda x : x**3)
print(Timer(c).timeit(2000))
