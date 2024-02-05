fint = open('q1i' , 'r')
cont = fint.readlines()

import numpy as np
def hilbert_mat(n):
    Amat=np.zeros([n,n])
    for i in range(0,n):
        for j in range(0,n):
            Amat[i][j] = (1/(i+j+1))    
            '''i + j + 1 bcoz index start from 0 '''
    trace = 0    
    for i in range(0,n):
        trace += Amat[i][i]
    return Amat,trace
output = []
cont1 = []
for line in cont:
    cont1.append(line.strip())

for line in cont1:
    
    output.append(str(hilbert_mat(int(line))[1])+ '\n')
fout = open('q1o' , 'w')
for i in output:
    fout.write(i)
fint.close()
fout.close()



