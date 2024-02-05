i=0
outp=open("tut1q14o.txt","w")
while (i<=10):
    i+=1
    outp.write( (str(i)+ " "+str( 2*3.14*((i/9.81)**0.5)))+"\n")
outp.close()
