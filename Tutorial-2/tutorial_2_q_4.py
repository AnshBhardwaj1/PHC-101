def bisection_method(func, a, b):

    def f(x):
        f = eval(func)
        return f
    error_accept = 0.000000001
    error = float(abs(b-a))

    while error > error_accept:
        c = (b+a)/2

        if f(a) * f(b) >= 0:
            print("No root present so bisection will not work")
            quit()

        elif f(c) * f(a) < 0:
            b = c
            error = abs(b-a)

        elif f(c) * f(b) < 0:
            a = b
            error = abs(b-a)

        else:
            print("Somethong went wrong")
            quit()

    print("The approx root is at : ", c)

func = input("f(x) : ") #input function as a string  ex- x**2
a = float(input("a : "))
b = float(input("b : "))
bisection_method(func, a, b)

