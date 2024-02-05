#Write a function which reads a one dimensional array and the number of elements, and returns the following quantities: (i) Maximum (ii) Minimum (iii) average (iv) standard deviation median (vi) sum of all the numbers and vii) product of all the numbers.
array=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    array.append(int(input("Enter the element: ")))
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
print("The maximum of the array is ",maximum(array))
print("The minimum of the array is ",minimum(array))
print("The average of the array is ",average(array))
print("The standard deviation of the array is ",standard_deviation(array))
print("The median of the array is ",median(array))
print("The sum of the array is ",sum(array))
print("The product of the array is ",product(array))
