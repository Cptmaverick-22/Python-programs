menu = {'Book': 300, 'Pen': 45, 'Notebook': 60, 'Geometry Box': 100, 'Markers': 50, 'Ruler': 15,'Colour Pencils': 200}
print(menu)
menu_lower = {i.lower(): menu[i] for i in menu}
total_amount = 0 
n = 1
while n>0:
    order = input("Enter the product you want to order (or type 'done' to finish): ")
    count = int(input("Enter the count: "))

    if order.lower() == 'done':
        break

    if order.lower() in menu_lower:
        total_amount = menu_lower[order.lower()]*count
    else:
        print("Product not present, re-enter your product")

print("Total amount:", total_amount)
