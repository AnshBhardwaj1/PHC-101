import numpy as np
def avg(x ,y ):
    return (x+y)/2

def fa(a):
    x = a**2 - 5 *a + 6
    return x


def biroot(a,b,f):  
    if f(a)*f(b) < 0:
        for i in range(0,1000):
            me = avg(a,b)
            if abs(a-b) < 0.001:
                print('Program exited after convergence')
                return me
            elif f(me)*f(a) > 0 :
                a = me
            elif f(me)*f(a) == 0:
                return me
            else :
                b = me  
    print('program exitted before convergence')
    return (a+b)/2
fint = open('input204','r')
cont = fint.readlines()
cont1 = []
for i in cont:
        cont1.append(i.split(  )) 
fout = open('output204','w')
for m in cont1:
        fout.write(f'root = {biroot(float(m[0]) ,float( m[1]) , fa )}\n')
fout.close()
fint.close()
