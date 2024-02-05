inp=open("tut1q4i.dat","r")

j1=int(inp.readline())
j2=int(inp.readline())
array=[]
for i in range(abs(j1-j2),j1+j2+1):
    array.append(i)
outp=open("tut1q4o.txt","w")
outp.write(str(array))
inp.close()
outp.close()
