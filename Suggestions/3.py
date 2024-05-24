a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))
l = a
if b > l:
    l = b
elif c > l:
    l = c

print("Greatest: ",l)


#Another Way

print("Maximum among 3 Numbers")
a = int(input("Enter the 1st Number: "))
b = int(input("Enter the 2nd Number: "))
c = int(input("Enter the 3rd NUmber: "))
if a>b and a>c:
    print("a is maximum",a)
elif b>c and b>a:
    print("b is maximum",b)
else:
    print("c is maximum",c)
