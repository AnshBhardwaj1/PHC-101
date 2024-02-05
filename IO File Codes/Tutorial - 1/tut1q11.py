inp=open("tut1q11i.dat","r")
Vs=float(inp.readline())
Rs=float(inp.readline())
Rl=float(inp.readline())

p = (Vs*Vs*Rl)/((Rl + Rs)*(Rl + Rs))
Rl=[i for i in range (1,11)]
outp=open("tut1q11o.txt","w")
for i in range (len(Rl)):
    outp.write("Power dissipation at "+str(Rl[i])+" is " +str((144*Rl[i])/((Rl[i] + 2.5)*(Rl[i] + 2.5)))+"\n")
outp.close
inp.close()

