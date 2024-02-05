import numpy as np

def new_rap(a , f , fd):
    for i in range(0,1000):
        if abs(f(a)) < 0.001:
            
            return a
        else :
            a  -=  f(a)/fd(a)
    print( "function did n't converged after given iterations")
    return a
def func(x):
  return x**3 - 6*x**2 + 11*x - 6
fder = lambda x : 3*x**2 - 12*x+11
fint = open('input205' , 'r')
cont = fint.readlines()
fout = open('output205','w')
for i in cont:
    fout.write('%9.4f\n'%(new_rap(float(i),func , fder)))
fout.close()
fint.close()
