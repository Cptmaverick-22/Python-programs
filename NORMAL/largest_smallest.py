a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

if(a>b and a>c):
    if(b<c):
        print("largest number: ",a)
        print("smallest number: ",c)
    else:
        print("largest number: ",a)
        print("smallest number: ",b)
elif(b>c):
    if(c<a):
        print("largest number: ",b)
        print("smallest number: ",c)
    else:
        print("largest number is: ",b)
        print("smallest number: ",a)
else:
    if(b<a):
        print("largest number: ",c)
        print("smallest number: ",b)
    else:
        print("largest number: ",c)
        print("smallest number: ",a)
