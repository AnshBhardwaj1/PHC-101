import numpy as np
import matplotlib.pyplot as plt
def inter_pol(x1 , x, y):
    n = len(x)
    value = 0
    for i in range(0,n):
        p = 1
        for k in range(0,n):
            if k == i :
                continue
            else:
                p *= (x1 - x[k])/(x[i] - x[k])
        value += p*y[i]
    return value
fint = open('input209','r')
cont = fint.readlines()
for i in range(0,len(cont)):
    cont[i] = eval(cont[i])
fout = open('output209','w')
for m in cont:
    far = []
    for k in m[-1]:
        far.append(inter_pol(k,m[1],m[2]))
    fout.write(f'{far}\n')



