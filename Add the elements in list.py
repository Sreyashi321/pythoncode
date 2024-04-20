#wapp to take a list and add the elements.
list=[]
n=int(input("Enter the number of terms:"))
for i in range(n):
    element=int(input("Enter element:"))
    list.append(element)
sum=0
for num in list:
    sum=sum+num
print("The total of the list:",sum)
