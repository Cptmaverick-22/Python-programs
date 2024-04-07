def apply_coupon(select, item_1, item_2,item_3,item_4,count):
    total = 0
    if select == 100:
        total = item_1*count
        if total <= 200:
            return "no coupon applied"
        elif total > 200 and total < 300:
            total -= 50
            return total
        elif total >= 300 and total <= 500:
            total -= 100
            return total
        elif total > 500:
            total -= 150
            return total
    elif select == 200:
        total = item_2*count
        if total <= 200:
            return "no coupon applied"
        elif total > 200 and total < 300:
            total -= 50
            return total
        elif total >= 300 and total <= 500:
            total -= 100
            return total
        elif total > 500:
            total -= 150
            return total
    elif select == 300:
        total = item_3*count
        if total <= 200:
            return "no coupon applied"
        elif total > 200 and total < 300:
            total -= 50
            return total
        elif total >= 300 and total <= 500:
            total -= 100
            return total
        elif total > 500:
            total -= 150
            return total
    elif select == 400:
        total = item_4*count
        if total <= 200:
            return "no coupon applied"
        elif total > 200 and total < 300:
            total -= 50
            return total
        elif total >= 300 and total <= 500:
            total -= 100
            return total
        elif total > 500:
            total -= 150
            return total
    else:
        return "Invalid selection"

item_1 = 100
item_2 = 200 
item_3 = 300
item_4 = 400
count = int(input("Enter the count: "))
select = int(input("Enter 100 or 200: "))

discount = apply_coupon(select, item_1,item_2,item_3,item_4,count)
print("Discounted price: ",discount)
