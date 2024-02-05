#Write a function which reads a one dimensional array and the number of elements, and returns the following quantities: (i) Maximum (ii) Minimum (iii) average (iv) standard deviation median (vi) sum of all the numbers and vii) product of all the numbers.
array=[]
inp=open("tut1q12i.dat","r")
n=int(inp.readline())
for i in range(n):
    array.append(int(inp.readline()))
def maximum(array):
    max=array[0]
    for i in array:
        if i>max:
            max=i
    return max
def minimum(array):
    min=array[0]
    for i in array:
        if i<min:
            min=i
    return min
def average(array):
    sum=0
    for i in array:
        sum+=i
    return sum/len(array)
def standard_deviation(array):
    sum=0
    for i in array:
        sum+=i
    mean=sum/len(array)
    sum=0
    for i in array:
        sum+=(i-mean)**2
    return (sum/len(array))**0.5
def median(array):
    array.sort()
    if len(array)%2==0:
        return (array[len(array)//2]+array[len(array)//2-1])/2
    else:
        return array[len(array)//2]
def sum(array):
    sum=0
    for i in array:
        sum+=i
    return sum
def product(array):
    product=1
    for i in array:
        product*=i
    return product
out=open("tut1q12o.txt","w")
out.write(("The maximum of the array is "+str(maximum(array)))+("\n"))
out.write(("The minimum of the array is "+str(minimum(array)))+("\n"))
out.write(("The average of the array is "+str(average(array)))+("\n"))
out.write(("The standard deviation of the array is "+str(standard_deviation(array)))+("\n"))
out.write(("The median of the array is "+str(median(array)))+("\n"))
out.write(("The sum of the array is "+str(sum(array)))+("\n"))
out.write(("The product of the array is "+str(product(array)))+("\n"))
out.close()
inp.close()

