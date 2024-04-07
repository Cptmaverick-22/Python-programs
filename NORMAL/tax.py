def tax(cp):
    if(cp > 100000):
        tax = cp*15/100
        print(tax)
    elif(cp > 50000 and cp<=100000):
        tax = cp*10/100
        print(tax)
    elif(cp<50000):
        tax = cp*5/100
        print(tax)

cp = int(input("Enter the cp: "))
tax(cp)
