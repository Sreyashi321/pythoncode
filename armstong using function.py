'''def armstrong(num):
    order=len(str(num))
    temp=num
    sum=0
    while temp>0:
        dig=temp%10
        sum=sum+dig**order
        temp=temp//10
    return num==sum
num=int(input("Enter any num:"))
if armstrong(num):
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")'''
def arms(num):
    n_str=str(num)
    power=len(n_str)
    sum=0
    for digit in n_str:
        sum=sum+int(digit)**power
    return sum==num
num=int(input("Enter any number:"))
if arms(num):
    print(num,"is armstong number")
else:
    print(num,"is not armstong number")
