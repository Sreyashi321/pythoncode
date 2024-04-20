'''n=int(input("Enter number of terms:"))
term=1
sum=0
for i in range(n):
    print(term, end=" ")
    term=term*10+1
for i in range(n):
    sum=sum+term
    term=term*10+1
print("\nSum is:", sum)'''













N = int(input("Enter the number of terms: "))
series_sum = 0
term = 1
for i in range(N):
    series_sum += term
    print(term, end=" ")
    term = term * 10 + 1
print("Sum of the series is:", series_sum)
'''N = int(input("Enter the number of terms: "))
num = 1

for i in range(N):
    print(num, end=" ")
    num = num * 10 + 1'''
