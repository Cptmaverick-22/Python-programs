print ("calculator")
print ("1: addition")
print ("2: subtraction")
print ("3: multiplication")
print ("4: division")

a = int(input("Enter A: "))
b = int(input("Enter B: "))

ch = int(input("enter your choice (1-4): "))
if ch == 1:
    c=a+b
    print("Addition: ",c)
elif ch == 2:
    c = a-b
    print("Subtraction: ",c)
elif ch == 3:
    c= a*b
    print("Multiplication: ",c)
elif ch == 4:
    c= a/b
    print("Division :",c)
else:
    print("wrong choice")