#Write a function which reads a one-dimensional array and the number of elements, and returns the following quantities: (i) Maximum (ii) Minimum and (iii) average.
n=int(input("Enter the number of elements: "))
array=[]
for i in range(n):
    array.append(int(input("Enter the element: ")))
def maxminavg(array):
    max=array[0]
    min=array[0]
    sum=0
    for i in range(n):
        if (array[i]>max):
            max=array[i]
        if (array[i]<min):
            min=array[i]
        sum+=array[i]
    avg=sum/n
    return max,min,avg
max,min,avg=maxminavg(array)
print("Maximum: ",max)
print("Minimum: ",min)
print("Average: ",avg)