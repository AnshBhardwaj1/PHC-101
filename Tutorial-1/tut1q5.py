n = int(input("Enter n : "))
x = float(input("Enter x : "))

def factorial(s):
	f = 1
	if(s == 0):
		return f
	for i in range(1, s + 1):
		f*=i
	return f

def cos(x, n):
	cos = 0
	for i in range(0, n+1):
		cos+=((-1)**i)*(x**(2*i))/factorial(2*i)
	return cos

def sin(x, n):
	sin  = 0
	for i in range(1, n+1):
		sin+=((-1)**(i+1))*(x**(2*i - 1))/factorial(2*i - 1)
	return sin

r = cos(x , n)
d = sin(x, n)

print ("Sin is ",d)
print ("Cos is ",r)

