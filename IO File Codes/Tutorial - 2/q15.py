import numpy as np
fint = open('input2014' , 'r')
cont = fint.readlines()
for i in range(len(cont)):
    cont[i] = eval(cont[i])
print(cont)
z = np.array([cont[0]])
w = np.array([cont[1]])
R = 6371
M = 500
def gravit_force(y):
  force = (9.81)*M*(R**2)/(R+y)**2
  return force
def simp(a , b , n , fun):
  h = (b-a)/n
  sum = fun(a)*h/3
  for i in range(1,n):
    sum += ((i%2) + 1)*2*fun(a + i*h)*h/3
  sum += fun(b)*h/3
  return sum
z = simp(0 , 800 , 80 , gravit_force)
print(z)
def gaussian(a ,b ,f ):
    an =((b - a)/2)*w*f(((b-a)/2)*z + (b+a)/2)
    return np.sum(an)
print(gaussian(0 ,800 , gravit_force))



