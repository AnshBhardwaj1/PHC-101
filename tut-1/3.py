#Write a program which reads x1, f (x1), x2, f (x2) and x, and returns the value of f (x). Assume that the three points (x, f (x)), (x2, f (x2)) and (x, f (x)) lie in the same line.
x1=int(input(""))
fx1=int(input(""))
x2=int(input(""))
fx2=int(input(""))
slope=(fx2-fx1)/(x2-x1)
x=int(input(""))
fx=x*slope
print (fx)