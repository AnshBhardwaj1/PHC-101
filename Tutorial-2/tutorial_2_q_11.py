def subroutine():
    def Input(n, x, y):

        for i in range (n):
            x.append(float(input("x" + str(i+1) + " : ")))
        for i in range (n):
            y.append(float(input("y" + str(i+1) + " : ")))

    def change(n, m, x, y, xp, yp, yd):    

        for i in range(m-1):
            c = (y[i+1] - y[i])/(x[i+1]-x[i])
            yp.append(c)
        
        for i in range(m):
            a = x[0] + i*(x[n-1] - x[0])/m
            xp.append(a)
        for i in range(m-2):
            b = (yp[i + 1] - yp[i])/(xp[i + 1]- xp[i])
            yd.append(b)
        

    n = int(input("n : "))
    x = []
    y = []
    xp = []
    yp = []
    yd = []
    Input(n, x, y)
    m = int(input("Enter m (m <= n) : "))
    change(n, m, x, y, xp, yp, yd)
    print(yp)
subroutine()