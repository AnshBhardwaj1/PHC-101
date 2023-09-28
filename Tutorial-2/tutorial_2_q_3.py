def func():
    a = []
    n = int(input("Length : "))
    for i in range(n):
        x = int(input("element " + str(i+1) + " : "))
        a.append(x)

    print( "max : ", max(a))
    print("average : ", sum(a)/n)
    print("min : ", min(a))

func()