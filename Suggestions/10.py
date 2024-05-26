num = int(input("Enter the number: "))
sum = 0
while(num>0):
    rem = num%10
    sum = sum+rem
    num = num//10
print("Sum of the digits: ",sum)

#Another Way:

num = int(input("Enter the Number: "))
n = str(num)
sum = 0
for (i) in n:
    sum = sum+int(i)
print(sum)