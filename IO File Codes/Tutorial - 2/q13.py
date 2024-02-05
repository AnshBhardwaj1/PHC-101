import numpy as np
def simp(a , b , n , fun):
    if  n %2 :
        raise ValueError('n should be even')
    h = (b-a)/n
    sum = fun(a) + fun(b)
    for i in range(1,n):
        sum += ((i%2) + 1)*2*fun(a + i*h)
    return sum*h/3
fa = lambda x : x**3
fint = open('q13i' , 'r')
cont = fint.readlines()
for m in range(len(cont)):
    cont[m] = eval(cont[m])

out = open('q13o' , 'w')
for i in range(len(cont)):
    a = cont[i][0]
    b = cont[i][1]
    n = cont[i][2]
    out.write(str(simp(a , b , n , fa)) + '\n')
print(cont)


