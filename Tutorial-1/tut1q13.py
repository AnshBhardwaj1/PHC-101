w = float(input("weight(in kg) : "))
h = float(input("height(in meters) : "))
bmi = w/(h*h)
bmi = float(bmi)
print(bmi)
if ( bmi < 25.0) :
	print"Griade 0 (desirable)"
elif  (bmi < 30.0) :
	print"Grade 1 (overweight)"
elif ( bmi <= 40.0) :
	print"Grade 2 (obese)"
else :
	print"Grade 3 (morbidly obese)"

