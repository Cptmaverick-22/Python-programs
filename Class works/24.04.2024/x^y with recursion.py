def power(x,y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x*power(x,y-1)

x = int(input("Enter the number: "))
y = int(input("Enter the number: "))
print("the value is: ",power(x,y))