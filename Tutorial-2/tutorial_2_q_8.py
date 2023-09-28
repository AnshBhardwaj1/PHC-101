def interpolate(m, x, y, xp) :
    yp = 0

    for i in range (m):
        p = 1
        for j in range (m):
            if( j != i):
                p *= (xp - x[j])/(x[i] - x[j])
        yp += y[i]*p

    #print
    print('For x = %.2f, y = %f' %(xp, yp))
m = int(input("n : "))
x = []
y = []

for i in range (m):
    x.append(float(input("x" + str(i+1) + " : ")))
for i in range (m):
    y.append(float(input("y" + str(i+1) + " : ")))
xp = float(input("Enter x : "))

interpolate(m, x, y, xp)