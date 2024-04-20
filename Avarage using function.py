'''def avg(numbers):
    total=sum(numbers)
    avar=total/len(numbers)
    return avar
input_n=input("Enter numbers:")
numbers=[int(num) for num in input_n.split()] #The split() method splits the string into a list of strings, where each string is a substring of the original string that is separated by a whitespace character.
result=avg(numbers) #The int() function converts each string in the list to an integer
print("Avarage is:",result)'''

def avg():
    number = input("Enter numbers separated by spaces:")
    num=number.split()
    total=0
    count=0
    for i in num:
        total=total+int(i)
        count=count+1
    avarage=total/count
    return avarage
result=avg()
print("The avarage of number is:",result)
