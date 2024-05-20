a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

l = a
s = a

if b>l:
    l=b
elif b<l:
    s = b

if c>l:
    l = c
elif c<l:
    s = c

print("largest: ",l)
print("Smallest: ",s)