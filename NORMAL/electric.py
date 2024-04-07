def electric(units):
    price = 0

    if units <= 100:
        price = 0
    elif units <= 200:
        price = (units - 100) * 5
    else:
        price = 100 * 5 + (units - 200) * 10

    return price

units = int(input("Enter the number of units consumed: "))
price = electric(units)
print(price)