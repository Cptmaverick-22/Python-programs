num = int(input("Enter a 4 digit number: "))
rev = 0
sum = 0
while num>0:
    remainder = num % 10  
    rev = (rev * 10) + remainder  
    num = num // 10  
    sum = remainder + sum
print("The reverse of the numbers: ",rev)
print("The total sum of digits is:",sum)


