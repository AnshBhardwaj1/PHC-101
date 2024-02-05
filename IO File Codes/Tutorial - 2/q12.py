import numpy as np
import matplotlib.pyplot as plt
def trap_int(a  , b , n ,func ) :
    h = (b - a )/n
    sum = 0
    for i in range(0,n+1):
        sum += (h)*(func(a + i*h))
    sum = sum - (h/2)*(func(a) + func(b))
    return sum 
a = float(input('Enter lower limit'))
b = float(input('Enter upper limit'))
n = int(input('Enter number of intervals'))
z = trap_int( a  , b  , n , lambda x : x**2)
print(z)

