outp = open("tut1q2o.txt", "w")
inp = open("tut1q2i.dat", "r")


o = int (inp.readline()) # o means order of matrix
matrix1 = []

for i in range(o):
    c = []
    for j in range(o):
        e=int(inp.readline())
        c.append(e)
    matrix1.append(c)

matrix2 = []


for i in range(o):
    c = []
    for j in range(o):
        e = int (inp.readline())
        c.append(e)
    matrix2.append(c)

matrix3 = []

for i in range(o):
    c = []
    for j in range(o):
        e = matrix1[i][j] + matrix2[i][j]
        c.append(e)
    matrix3.append(c)
    
matrix4 = [] # matrix4 is product matrix
for i in range(o):
     c = []
     for j in range(o):
         e = 0
         c.append(e)
     matrix4.append(c)

for i in range(o):
    for j in range(o):
        for k in range(o):
            matrix4[i][j]+=matrix1[i][k]*matrix2[k][j]

outp.write(("Sum : \n"))
for i in range(o):
    
    outp.write(str(matrix3[i])+"\n")
 
        
outp.write(("Product : \n"))    
for i in range(o):
    
    outp.write(str(matrix4[i])+"\n")


