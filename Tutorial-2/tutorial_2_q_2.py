n = int(input("length : "))
a = []
for i in range(n):
	b = int(input("element " + str(i+1) + " : "))
	a.append(b)

for round in range (n):
	for i in range (n-round-1):
		if (a[i] < a[i +1]):
			temp = a[i]
			a[i] = a[i + 1]
			a[i + 1] = temp

print(a)


