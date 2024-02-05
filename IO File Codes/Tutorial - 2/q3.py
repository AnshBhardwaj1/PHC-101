fint = open('input203' , 'r')
cont = fint.readlines()
cont1 = []
for i in cont :
    i1 = i.split()
    cont1.append([i1[0],eval(i1[1])])
def maxmin(L):
    max1 = L[0]
    min1 = L[0]
    for i in L :
        if i > max1 :
            max1 = i
        if i < min1 :
            min1 = i
    return max1, min1
fout = open('output203' , 'w')
for m in cont1 :
    max1 , min1 = maxmin(m[1])
    fout.write(f'max = {max1} , min = {min1} \n')
fout.close()
fint.close()



