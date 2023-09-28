n = (input("length of array : "))
arr = []

for i in range(0, n):
    x = float(input("Enter element : "))
    arr.append(x)

def max(n):
    max = arr[0]
    for i in range(1, n):
        if(arr[i] > max):
            max = arr[i]
    return max

def min(n):
    min = arr[0]
    for i in range(1, n):
        if(arr[i] < min):
            min = arr[i]
    return min

def average(n):
    sum = 0
    for i in range(0, n):
        sum+=arr[i]
    average = sum/n
    return average

def sum(n):
    sum = 0
    for i in range(n):
        sum+=arr[i]
    return sum
def product(n):
    product = 1
    for i in range(0, n):
        product*=arr[i]
    return product
def median(n):
	for r in range(n):
	    for i in range(n - r - 1):
        	if(arr[i] < arr[i+1]):
            		temp = arr[i+1]
            		arr[i+1] = arr[i]
            		arr[i] = temp
	if(n%2 == 0):
	     return ((arr[int(n/2 - 1)]+arr[int(n/2)])/2)
	else:
		return (arr[int((n+1)/2-1)])
def st_dev(n):
	sum = 0
        for i in range(0):
		sum+=arr[i]
	avg = sum/n
	ans = 0
	for i in range(n):
		ans+=((arr[i]-avg)**2)/n
	return ans
print"max : ", max(n)
print"min : ", min(n)
print"average : ", average(n)
print"sum : ", sum(n)
print"product : ", product(n)
print"median : ", median(n) 
print"standard deviation : ", st_dev(n)
    
