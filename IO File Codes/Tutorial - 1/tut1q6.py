ln2,v2=0,0
for i in range(1,10000):
    ln2+=((-1)**i)/i
outp=open("tut1q6o.txt","w")

outp.write("Value of -ln2 is : "+str(ln2)+"\n")
for i in range(1,10000):
    v2+=1/((i)*(i+1))

outp.write("Value of 2 is : "+str(v2))
outp.close()
