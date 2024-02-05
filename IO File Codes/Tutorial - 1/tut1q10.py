inp=open("tut1q10i.dat","r")
a1=float(inp.readline())
a2=float(inp.readline())
g=float(inp.readline())
inp.close()

if(a1 == a2):
    if(g == 90.0):
        out='Square'
    elif(g == 120.0):
        out= ("Hexagonal")
    else:
        out= ("Invalid g")
elif(g == 90.0):
    out= ("Rectangular or Centered Rectangular")
elif(g == 120):
    out= ("Invalid g")
else:
    out= ("Oblique")
outp=open("tut1q10o.txt","w")
outp.write(out)
outp.close()

