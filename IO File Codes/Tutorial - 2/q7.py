import numpy as np
g = 9.81
fint = open('input207' , 'r')
cont = fint.readlines()
for i in range(len(cont)):
    m  = (cont[i].strip()).split('  ')
    for k in range(len(m)):
        m[k] = eval(m[k].lstrip())
    cont[i] = m 
print(cont)
def bracket_root(f , x_0 , h =0.1 , max_iter = 100 , direction = 1 ):
  a , b = x_0   , x_0  + direction*h
  fa , fb = f(a) , f(b)
  if abs(fb) > abs(fa):
    direction *= -1
    b = x_0 + direction*h
    fb = f(b) 
  for _ in range(max_iter):
    if f(a)*f(b) < 0 :
      return (a,b)
    a , b = b , b + h*direction
  raise Exception('Interval not found') 
def biroot(a,b,f , tol = 1e-3, max_iter = 100  ):
    if f(a)*f(b) > 0 :
        raise ValueError("f(a) and f(b) should have opposite signs")
    for _ in range(max_iter):
        c = (a + b)/2
        if abs(a-b) < tol :
            return c
        if f(c)*f(a) > 0 : 
            a = c
        else : 
            b = c
    raise Exception('Function did not converged in given no. of iterations')

fout = open('output207' , 'w')
for i in cont:
    func = lambda x : np.sin(x) - np.sqrt(2*g*i[1] /(i[0]**2))
    game = bracket_root(func, i[2])
    ans = biroot(game[0] , game[1] , func )
    fout.write(f'{ans}\n')
fout.close()

