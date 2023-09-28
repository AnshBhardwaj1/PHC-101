def f(y):
    m = 500
    g0 = 9.81
    R = 6371000 #in meters

    return (m*g0*(R**2))/(R + y)**2

a = 0 # lower limit
b = 800000 # upper limit
n = 1000
h = (b-a)/n
sum = 0

for i in range (1, n):
        y = a + i*h
        if(i%2 == 0):
            sum += 2*f(y)
        else:
            sum += 4*f(y) 
ans = (h/3)*(f(a) + f(b) + sum)

print(ans)


