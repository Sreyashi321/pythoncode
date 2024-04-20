Low=int(input("Enter lower range:"))
Upp=int(input("Enter upper range:"))
print("The numbers are:")
for num in range(Low,Upp+1):
    order=len(str(num))
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp=temp//10
    if sum==num:
        print(num)




