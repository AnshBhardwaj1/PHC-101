n = int(input("n : "))
sum = 0
for i in range(1,n+1):
	sum+=i
	i+=1
print(sum)

formula = n*(n+1)/2
print "by formula : ", formula

