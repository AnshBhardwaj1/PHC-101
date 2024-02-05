inp=open("tut1q8i.dat","r")
n1=float(inp.readline())
n2=float(inp.readline())
D=float(inp.readline())
l=float(inp.readline())

ans = 0.5*((3.14*D*(n1**2 - n2**2)**0.5)/l)
outp=open("tut1q8o.txt","w")
outp.write("Focal length is : "+str(ans))
inp.close()
outp.close()

