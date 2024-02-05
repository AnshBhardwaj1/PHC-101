
def secantMethod(a , b ,f ):
    def f(x):
        f = eval(func)
        return f
    for i in range(0,1000):
        d = f(b)
        if abs(f(a)) < 0.001 :
            return a
        c = f(a)
        phi = a
        a -=  c*(a - b)/(c - d)
        b = phi
        d = c
    print('function did not convergered after given iterations')
    return a

func = input("Enter the function : ") #input function as a string  ex- x**2
x0 = int(input("x0 : "))
x1 = int(input("x1 : "))

print (secantMethod( x0, x1,func))


