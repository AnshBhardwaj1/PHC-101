def subroutine():
    def Input(n, x, y):

        for i in range (n):
            x.append(float(input("x" + str(i+1) + " : ")))
        for i in range (n):
            y.append(float(input("y" + str(i+1) + " : ")))

    def change(n, x, y, yp):    

        for i in range(n-1):
            c = (y[i+1] - y[i])/(x[i+1]-x[i])
            yp.append(c)

    n = int(input("n : "))
    x = []
    y = []
    yp = []
    Input(n, x, y)
    change(n, x, y, yp)
    print(yp)
subroutine()