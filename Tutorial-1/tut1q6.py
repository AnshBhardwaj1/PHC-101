a = 0
b = 0
for n in range(1, 10000000):
	a+=((-1)**n)/n
	b+=(1/(n*(n+1)))
print a, b

