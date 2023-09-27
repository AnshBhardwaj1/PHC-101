#Write a program to read an array (row matrix) of numbers along with the size of the array.
#The output of this program should be the array sorted in descending order
size=int(input("Enter the size of the array: "))
array=[]
for i in range(size):
    array.append(int(input("Enter the element: ")))
array.sort(reverse=True)
for i in range(size):
    print(array[i],end=" ")
