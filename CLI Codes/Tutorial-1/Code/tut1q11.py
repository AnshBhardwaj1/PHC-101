
Vs = int(input("Vs : "))
Rs = int(input("Rs : "))
Rl = int(input("Rl : "))
p = (Vs*Vs*Rl)/((Rl + Rs)*(Rl + Rs))
print ("power : " , p)
Rl=[i for i in range (1,11)]
for i in range (len(Rl)):
    
    print ("Power dissipation at",Rl[i],"is" ,(144*Rl[i])/((Rl[i] + 2.5)*(Rl[i] + 2.5)))
