import math
a = (int(input("Enter a : ")))
b = (int(input("Enter b : ")))
c = (int(input("Enter c : ")))

cosA = ((b**2) + (c**2) - (a**2))/(2*b*c)
cosB = ((a**2) + (c**2) - (b**2))/(2*a*c)
cosC = ((b**2) + (a**2) - (c**2))/(2*b*a)

A = math.acos(cosA)
B = math.acos(cosB)
C = math.acos(cosC)

print ("Angle A : ", A)
print ("Angle B : ", B)
print ("Angle C : ", C)
