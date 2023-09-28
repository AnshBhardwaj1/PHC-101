j1 = int(input("j1 : "))
j2 = int(input("j2 : "))
a = 0
b = 0
if j1 > j2 :
	 a = abs(j1 - j2)
	 b = j1 + j2
if a > b :
         temp = a
	 a = b
	 b = temp
for i in range(a, (b+1), 1):
	 print(a)
	 a+=1
