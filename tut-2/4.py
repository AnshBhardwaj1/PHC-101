#n the bisection method to find the root of a function f (x) in the interval (a, b), the approximate root in an iteration “i is given by x i = (x+ + x−)/2, where f (x+ ) > 0 and f (x−) < 0.
#Write a function program whose inputs are a, b (the initial guess) and the function f (x). The function should return the root x r of the equation f (x) = 0
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
print ("Please edit the function in the code to change the function")
def f(x):
    return (x**2-2)
def root(a,b):
    x=(a+b)/2
    while (abs(f(x))>0.0001):
        if (f(x)>0):
            b=x
        else:
            a=x
        x=(a+b)/2
    return x
print(root(a,b))
