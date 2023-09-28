def secantMethod(func, x0, x1):

    def f(x):
        f = eval(func)
        return f

    for intercept in range(1, 10):
        fx0 = f(x0)
        fx1 = f(x1)
        xi = x0 - (fx0 / ((fx0 - fx1) / (x0 - x1)))

        x0 = x1
        x1 = xi

    print("The root is at : ", xi)

func = input("Enter the function : ") #input function as a string  ex- x**2
x0 = int(input("x0 : "))
x1 = int(input("x1 : "))

secantMethod(func, x0, x1)