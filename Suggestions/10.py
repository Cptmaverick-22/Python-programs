num=int(input("Enter a number:"))
sum=0
while(num>0):
    d=num%10
    sum=sum+d
    num=num//10
print("The total sum of digits is:",sum)

#Another Way:

num = int(input("Enter the Number: "))
n = str(num)
sum = 0
for (i) in n:
    sum = sum+int(i)
print(sum)