#Write a program which reads two matrices and return the sum and product of the two matrices
matrix1=[]
matrix2=[]
sum=[]
product=[]
print("Enter the elements of the first matrix")
for i in range(0,3):
    matrix1.append([])
    for j in range(0,3):
        matrix1[i].append(int(input()))
print("Enter the elements of the second matrix")
for i in range(0,3):
    matrix2.append([])
    for j in range(0,3):
        matrix2[i].append(int(input()))
for i in range(0,3):
    sum.append([])
    for j in range(0,3):
        sum[i].append(matrix1[i][j]+matrix2[i][j])
for i in range(0,3):
    product.append([])
    for j in range(0,3):
        product[i].append(matrix1[i][j]*matrix2[i][j])
print("The sum of the two matrices is ",sum)
print("The product of the two matrices is ",product)
