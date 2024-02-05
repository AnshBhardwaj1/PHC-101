import matplotlib.pyplot as plt
import numpy as np
inp=open("input.txt",'r')
xlistm=inp.readline()[1:-2].split(',')
xlistf=[]
for i in xlistm:
    xlistf.append(int(i))
ylistm=inp.readline()[1:-1].split(',')
ylistf=[]
for i in ylistm:
    ylistf.append(int(i))
xlist=np.array(xlistf)
ylist=np.array(ylistf)
def LSFit_line(L1,L2):
    n=len(L1)
    v1=(n*sum(L1*L2)-sum(L2)*sum(L1))/((n*sum(L1**2)-(sum(L1))**2))
    v2=(sum(L2)-v1*sum(L1))/n
    return v1,v2
a,b=LSFit_line(xlist,ylist)
print ("a =",a)
print ("b =",b)

plt.plot(xlist,ylist)
plt.scatter(xlist, ylist, color='red')
plt.xlabel('X---->')
plt.ylabel('Y---->')
plt.title("Eqaution Fitting")
plt.text(2,20,"y="+str(a)+"x+"+str(b))
plt.text(2,19,"a ="+str(a))
plt.text(2,18,"b ="+str(b))
plt.show()
f=open('out.txt','w')
f.write("a="+str(a)+"\n")
f.write("b="+str(b))
f.close()