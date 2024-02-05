#Your body mass index (BMI) is given by your weight (in kilos) divided by your height (in metres) squared. Write a program to read the weight and height and print out the BMI for each person
inp=open("tut1q13i.dat","r")
weight=float(inp.readline())
height=float(inp.readline())
BMI=weight/(height**2)
if (BMI>40):
    outpu= ("morbidly obese")
elif (BMI>30):
    outpu= ("obese")
elif (BMI>25):
    outpu= ("overweight")
elif (BMI>20):
    outpu= ("desirable")
outp=open("tut1q13o.txt","w")
outp.write("BMI is "+str(BMI)+" and is "+outpu)
outp.close()
inp.close()