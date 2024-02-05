def interpolateAndPrint(n, x, y, m, xp) :
    for k in range(m):
        yp = 0

        for i in range (n):
            p = 1
            for j in range (n):
                if( j != i):
                    p *= (xp[k] - x[j])/(x[i] - x[j])
            yp += y[i]*p

        #print
        print("yp" + str(k + 1) + " : ", yp)
n = int(input("n : "))
x = []
y = []

for i in range (n):
    x.append(float(input("x" + str(i+1) + " : ")))
for i in range (n):
    y.append(float(input("y" + str(i+1) + " : ")))

m = int(input("m : "))
xp = []
for i in range (m):
    xp.append(float(input("xp" + str(i+1) + " : ")))

interpolateAndPrint(n, x, y, m, xp)