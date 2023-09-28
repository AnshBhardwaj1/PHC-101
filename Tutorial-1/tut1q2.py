o = int(input("Enter order of matrix : ")) # o means order

matrix1 = []

print("For Matrix1 : ")

for i in range(o):
    c = []
    for j in range(o):
        e = int(input("Enter element " + str(i)+ " " + str(j)+ " : "))
        c.append(e)
    matrix1.append(c)

matrix2 = []

print("For Matrix2 : ")

for i in range(o):
    c = []
    for j in range(o):
        e = int(input("Enter element " + str(i) +" "+ str(j) +" : " ))
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

print("Sum : ")
for i in range(o):
    
        print matrix3[i]
 
        
print("Product : ")    
for i in range(o):
    
        print matrix4[i] 


