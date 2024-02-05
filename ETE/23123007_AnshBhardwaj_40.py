import scipy
import numpy as np
import time
from matplotlib import pyplot as plt

#b
x=np.arange(1,3,0.0000001)
y= (3*x*x) - 10
#-3x^2 gets cancelled from both sides therefore p=integration of (3x^2-10) from 1 to 3
p=scipy.integrate.simpson(y,x,0.01)
print ("Value of P is : ",p)

#c
def func(x):
    return -3*x*x + p
def func_deriv(x):
    return -6*x

#d
def Newton_method(f,df,x,tol,iterations):
    for _ in range(iterations):
        xc = f(x) / df(x)
        x -= xc
        if abs(xc) < tol: return x
    raise Exception ("No convergence in 100 iterations")

def Secant_method (f,x0,x1,tol,max_iter):
    fx0 = f(x0)
    for i in range(max_iter):
        fx1 = f(x1)
        x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
        fx0 = fx1
    raise Exception("No convergence in 100 iterations.")

#a
new=Newton_method(func,func_deriv,x.all(),tol=1e-9,iterations=100)
print ("Root of -3x^2 + p  is : ",new)

#e and f
tols=[0.5,0.1,0.05,0.01,1e-3,1e-6,1e-9]
t1l=[]
t2l=[]
outp=open('23123007.out','w')
for i in tols:
    sec_start_time = time.time()
    sec=Secant_method(func,1,3,i,100)
    sec_end_time = time.time()
    sec_time_taken=sec_end_time-sec_start_time
    new_start_time = time.time()
    new=Newton_method(func,func_deriv,x.all(),i,100)
    new_end_time = time.time()
    new_time_taken=new_end_time-new_start_time
    print ("Root when tolerance =",i, "using Newton Raphson is",new)
    print ("Root when tolerance =",i, "using Secant is ",sec)
    outp.write(str("for E= "+str(i)+" t1="+str(new_time_taken)+" t2="+str(sec_time_taken)+" t1-t2="+str(new_time_taken-sec_time_taken)+"\n"))
    t1l.append(new_time_taken)
    t2l.append(sec_time_taken)

#h
new=Newton_method(func,func_deriv,x.all(),tol=1e-9,iterations=100)
sec=Secant_method(func,1,3,tol=1e-9,max_iter=100)
outp.write("\nFor E=1e-9 \n")
outp.write("Root by Newton_raphson is : "+str(new)+"\n")
outp.write("Root by Secant is : "+str(sec)+"\n")
outp.write("Difference is "+str(sec-new)+"\n")
outp.close()



#Plotting
#i
newx=np.arange(-2,3,0.001)
plt.plot(newx,func(newx),label="f(x)=-3x^2+P \n P=6")
plt.scatter(-new,0)
plt.scatter(new,0)
plt.xlabel("X--->")
plt.ylabel(("f(x)--->"))
plt.title("x vs f(x) graph")
plt.legend()
plt.show()

#j
plt.plot(tols,t1l, label="t1 = Newton-Raphson")
plt.plot(tols,t2l,color="red", label="t2 = Secant")
plt.xlabel("Tolerance--->")
plt.ylabel("Time Taken--->")
plt.title("t1 and t2 vs Tolerance graph")
for i in range(len(tols)):
    plt.scatter(tols[i],t1l[i])
    #plt.text(tols[i],t1l[i],str(str(tols[i])+str(t1l[i])))
    plt.scatter(tols[i],t2l[i])
    #plt.text(tols[i],t2l[i],str(str(tols[i])+str(t2l[i])))
plt.legend()
plt.show()