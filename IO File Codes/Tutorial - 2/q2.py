import numpy as np
fint = open('input202' , 'r')
cont = fint.readlines()
cont1 = []
for line in cont:
  cont1.append((line.strip()).split('  '))

for l in cont1 :
    l[1] = eval(l[1])

def sorter(L):
  n = len(L)
  for i in range(0,n):
    for j in range(n-1 , i , -1):
        L[j] = float(L[j])
        L[j-1] = float(L[j-1])
        if L[j] > L[j-1]:
          a = L[j]
          L[j] = L[j-1]
          L[j-1] = a
  return L
fout = open('output202','w')
for li in cont1:
    fout.write('size = ' + li[0] + ' ')
    fout.write(f'sorted array = {sorter(li[1])}\n')
fout.close()
fint.close()

  
