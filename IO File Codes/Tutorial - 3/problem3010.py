import numpy as np
import matplotlib.pyplot as plt
fint = open('input3010' , 'r')
cont = fint.readlines()
n = len(cont)
for i in range(len(cont)):
  cont[i] = eval(cont[i].strip())
for i in range(n):
  c = cont[i][0]
  v = cont[i][1]
  q = c*v
  E = (1/2)*c*v**2
  cont[i] = [c , v , q , E]
fout = open('output3010' , 'w')
for i in cont :
    fout.write(f'{i}\n')
fout.close()
