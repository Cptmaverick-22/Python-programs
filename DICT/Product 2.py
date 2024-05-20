def apply_coupon(total_amount):
    if total_amount <= 100:
        return total_amount
    elif total_amount >100 and total_amount <=200:
        return total_amount-50
    elif total_amount >200 and total_amount <=400:
        return total_amount-70
    elif total_amount >400 and total_amount <=600:
        return total_amount-90
    elif total_amount>600 and total_amount <=900:
        return total_amount-110
    elif total_amount>100:
        return total_amount-170


menu = {'Book': 300, 'Pen': 45, 'Notebook': 60, 'Geometry Box': 100, 'Markers': 50, 'Ruler': 15, 'Colour Pencils': 200}
print(menu)
menu_lower = {i.lower(): menu[i] for i in menu}
total_amount = 0 
n = 1
while n > 0:
    order = input("Enter the product you want to order (or type 'done' to finish): ")

    if order.lower() == 'done':
        break
    
    count = int(input("Enter the count: "))

    if order.lower() in menu_lower:
        total_amount += menu_lower[order.lower()] * count
        apply_coupon(total_amount)
    else:
        print("Product not present, re-enter your product")
        
final_amount = apply_coupon(total_amount)

print("Total amount:", final_amount)
