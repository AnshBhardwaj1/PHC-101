x = int(input("Enter order of matrix : "))

ans = 0
for i in range(1, x+1):
    j=float(i)
    ans+=1/((2*j)-1)
print ("Trace of Hilbert matrix of order", x, "is ",  ans)
