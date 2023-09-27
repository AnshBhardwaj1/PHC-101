#the matrix with elements Hi j = 1/(i + j − 1) is called the Hilbert matrix. Write a program which returns the trace of any n × n Hilbert matrix where n is the input for the program.
n=int(input(""))
array=[]
for i in range(1,n+1):
    array.append([])
    for j in range(1,n+1):
        array[i-1].append(1/(i+j-1))
trace=0
for i in range(n):
    trace+=array[i][i]
print(trace)
