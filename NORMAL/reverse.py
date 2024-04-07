n = int(input("Enter the integer number: "))   
rev = 0  
while (n > 0):  
    remainder = n % 10  
    rev = (rev * 10) + remainder  
    n = n // 10  
print("The reverse number is :",rev)