import math
inp=open("tut1q9i.dat","r")

a=float(inp.readline())
b=float(inp.readline())
c=float(inp.readline())

cosA = ((b**2) + (c**2) - (a**2))/(2*b*c)
cosB = ((a**2) + (c**2) - (b**2))/(2*a*c)
cosC = ((b**2) + (a**2) - (c**2))/(2*b*a)

A = math.acos(cosA)
B = math.acos(cosB)
C = math.acos(cosC)

outp=open("tut1q9o.txt","w")
outp.write("Angle A : "+str(A)+"\n")
outp.write("Angle B : "+str(B)+"\n")
outp.write("Angle C : "+str(C)+"\n")
inp.close()
outp.close()

