#integrate x*e^-x from -3 to 3using simpsons rule and take input from xy.dat
input_file = open('xy.dat','r')
x=[]
for line in input_file:
    x.append(float(line.split()[0]))
#for n=1
def simpson(x):
    h=6/2
    return h*(x[0]+4*x[1]+x[2])/3
outp=open('23123007.out','w')
outp.write("For n=1\n")
outp.write("Value of integral is : "+str(simpson(x))+"\n")
#for n=2
outp.write("For n=2\n")
outp.write("Value of integral is : "+str(simpson(x[0:3])+simpson(x[2:5]))+"\n")
#for n=3
outp.write("For n=3\n")
outp.write("Value of integral is : "+str(simpson(x[0:3])+simpson(x[2:5])+simpson(x[4:7]))+"\n")
outp.close()
#plotting
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-3,3,0.01)
y1=(x)*np.exp(-x)
y2=(x*x)*np.exp(-x)
y3=(x*x*x)*np.exp(-x)
plt.plot(x,y1,label="x*e^-x")
plt.plot(x,y2,label="x^2*e^-x")
plt.plot(x,y3,label="x^3*e^-x")
plt.legend()
plt.show()