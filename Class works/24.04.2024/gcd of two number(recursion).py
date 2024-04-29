def gcd_rec(num1,num2):
    if (num1 % num2 == 0):
        return num2
    else:
        return(gcd_rec(num2,num1%num2))
    
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
print("GCD of the two numbers: ",gcd_rec(num1,num2))

