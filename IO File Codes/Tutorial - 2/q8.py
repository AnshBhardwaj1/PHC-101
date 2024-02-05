import numpy as np
import matplotlib.pyplot as plt


def inter_pol(x1,x,y):
  n = len(x)
  fun = 0
  for i in range(0,n):
    p = y[i]
    for k in range(0,n):
      if k == i:
        continue
      p *= (x1-x[k])/(x[i] - x[k])
    fun += p
  return fun
fint = open('input208','r')
cont = fint.readlines()
for i in range(0,len(cont)):
    cont[i] = eval(cont[i])
fout = open('output208','w')
for m in cont:
    fout.write('%9.4f\n'%(inter_pol(m[3],m[1],m[2])))
fout.close()
fint.close()






