#Write a program which reads j1 and j2 and returns the output as an array of values from | j1 − j2| to j1 + j2 in steps of unity.
j1=int(input(""))
j2=int(input(""))
array=[]
for i in range(abs(j1-j2),j1+j2+1):
    array.append(i)
print(array)
