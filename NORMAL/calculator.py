print ("calculator")
print ("1: addition")
print ("2: subtraction")
print ("3: multiplication")
print ("4: division")

a = int(input("Enter A: "))
b = int(input("Enter B: "))
print ("enter your choice (1-4)")
ch = int(input("enter the value: "))
if ch == 1:
    c=a+b
    print(c)
elif ch == 2:
    c = a-b
    print(c)
elif ch == 3:
    c= a*b
    print(c)
elif ch == 4:
    c= a/b
    print(c)
else:
    print("wrong choice")