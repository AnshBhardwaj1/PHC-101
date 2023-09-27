#Your body mass index (BMI) is given by your weight (in kilos) divided by your height (in metres) squared. Write a program to read the weight and height and print out the BMI for each person
weight=int(input("Enter your weight in kilograms: "))
height=int(input("Enter your height in metres: "))
BMI=weight/(height**2)
if (BMI>40):
    print (" morbidly obese")
elif (BMI>30):
    print (" obese")
elif (BMI>25):
    print (" overweight")
elif (BMI>20):
    print ("Desirable")