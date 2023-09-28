a1 = float(input("a1 : "))
a2 = float(input("a2 : "))
g = float(input("g : "))

if(a1 == a2):
    if(g == 90.0):
        print ("Square")
    elif(g == 120.0):
        print ("Hexagonal")
    else:
        print ("Invalid g")
elif(g == 90.0):
    print ("Rectangular or Centered Rectangular")
elif(g == 120):
    print ("Invalid g")
else:
    print ("Oblique")

