
fint = open('input2010' , 'r')
cont1 = fint.readlines()
for i in range(len(cont1)):
    cont1[i]=eval( cont1[i].strip())
n = len(cont1[1])
ydif = []
for i in range(1 , n - 1 ):
  ydif.append(float((cont1[1][i] - cont1[1][i-1])/(cont1[0][i] - cont1[0][i-1])))
print(ydif)
fout = open('output2010' ,'w')
fout.write(f'{ydif}')
fout.close()
