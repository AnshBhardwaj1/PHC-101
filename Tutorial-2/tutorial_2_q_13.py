def simpson(a, b, n, func):

    def f(x):
        f = eval(func)
        return f
    
    h = (b-a)/n
    sum = 0

    for i in range (1, n):
        x = a + i*h
        if(i%2 == 0):
            sum += 2*f(x)
        else:
            sum += 4*f(x) 
    ans = (h/3)*(f(a) + f(b) + sum)

    print(ans)

a = float(input("a : "))
b = float(input("b : "))
n = int(input("n : "))
func = input("f(x) : ")

simpson(a, b, n, func)
    