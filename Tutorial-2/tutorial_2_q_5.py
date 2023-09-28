def newton(fx, dfx, x):
    
    def f(x):
        f = eval(fx)
        return f
    def df(x):
        df = eval(dfx)
        return df

    for i in range (n):
        intercept = x - (f(x)/df(x))
        x = intercept

    print("ans : ", x)

fx = input("f(x) : ")
dfx = input("f'(x) : ")
n = int(input("n : "))

newton(fx, dfx, n)