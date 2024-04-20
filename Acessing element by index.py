list=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
    print(list)
pos=int(input("Enter the postion: "))
list=list[pos]
print("The element in entered postion: ")
print(list)

