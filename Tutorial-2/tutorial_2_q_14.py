def gauss(fx, a, b):
    
    def f(x):
        f = eval(fx)
        return f
    
    w = [128/225,(322+13*(70)**0.52)/900,(322+13*(70)**0.52)/900,(322-13*(70)**0.5)/900,(322-13*(70)**0.5)/900]
    z = [0,((5-2*(10/7)**0.5)**0.5)/3,-((5-2*(10/7)**0.5)**0.5)/3,((5+2*(10/7)**0.5)**0.5)/3,-((5+2*(10/7)**0.5)**0.5)/3]
    n = 5
    subAns = 1
    for i in range(0,n):
        subAns += w[i]*f((b-a)/2*z[i] + (b+a)/2)
    
    ans = (b-a)/2 * subAns
    return ans

f = input("f(x) : ") #input funxtion as a string
a = float(input("a : "))
b = float(input("b : "))

answer = gauss(f, a, b)
print(answer)
