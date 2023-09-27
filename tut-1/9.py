#Write a program to find the angles in an arbitrary triangle, given the lengths of the three sides. If you use the law of cosines you will find it helpful to know that the built-in function ACOS(X) returns the angle, in radians, whose cosine is X
side1=int(input("Enter the length of side 1: "))
side2=int(input("Enter the length of side 2: "))
side3=int(input("Enter the length of side 3: "))
import math
angle1=math.acos((side2**2+side3**2-side1**2)/(2*side2*side3))
angle2=math.acos((side1**2+side3**2-side2**2)/(2*side1*side3))
angle3=math.acos((side2**2+side1**2-side3**2)/(2*side2*side1))
print("The angles of the triangle are: ",angle1,angle2,angle3)
