import numpy as np
def sec_root(a , b ,f ):
    for i in range(0,1000):
        d = f(b)
        if abs(f(a)) < 0.001 :
            return a
        c = f(a)
        phi = a
        a -=  c*(a - b)/(c - d)
        b = phi
        d = c
    print('function did not convergered after given iterations')
    return a

f = lambda x : x**2 - 5*x + 6
fint = open('input206' , 'r')
cont = fint.readlines()
for i in range(0,len(cont)) :
    cont[i] = cont[i].split('  ')
fout = open('output206' , 'w')
for m in cont:
    fout.write('%9.4f\n'%(sec_root(float(m[0]),float(m[1]) , f)))
fout.close()
fint.close()

