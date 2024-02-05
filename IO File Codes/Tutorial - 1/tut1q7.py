ninp=open("tut1q7i.txt","r")
n=int(ninp.readline())
sum = 0
for i in range(1,n+1):
	sum+=i
	i+=1
outp=open("tut1q7o.txt","w")
outp.write("Sum is "+str(sum)+"\n")


formula = n*(n+1)/2

outp.write("By formula : "+str(formula))
ninp.close()
outp.close()


