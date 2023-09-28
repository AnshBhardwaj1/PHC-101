#In the bisection method to find the root of a function f (x) in the interval (a, b), the approx-
#imate root in an iteration “i is given by x i = (x+ + x−)/2, where f (x+ ) > 0 and f (x−) < 0.
#Write a function program whose inputs are a, b (the initial guess) and the function f (x). The
#function should return the root x r of the equation f (x) = 0.
def bisection (a, b, fx):
    def f(x):
        f = eval(fx)
        return f
    for i in range (10000):
        x = (a + b)/2
        if f(x) > 0:
            b = x
        else:
            a = x
    print("ans : ", x)
fx = input("f(x) : ")
a = int(input("a : "))
b = int(input("b : "))
bisection(a, b, fx)

