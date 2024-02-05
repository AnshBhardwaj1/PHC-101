import numpy as np
import matplotlib.pyplot as plt
fint = open('input308' , 'r')
cont = fint.readlines()
for i in range(0 , len(cont)):
    cont[i] = (cont[i].strip()).split(',')
    for j in range(len(cont[i])):
        cont[i][j] = float(cont[i][j])
cont = np.array(cont)
shap = cont.shape
trans = np.empty((shap[1] , shap[0]))
for i in range(shap[1]):
    for j in range(shap[0]):
        trans[i][j] = cont[j][i]
fout = open('output308' , 'w')
for i in trans :
    fout.write(f'{i}\n')
fout.close()
