def product():
    menu = {'Book':300, 'Pen':45, 'Notebook':60, 'Geometry Box':100, 'Markers':50, 'Ruler':15, 'Colour Pencils':200}
    print(menu)
    order = input("Enter the product you want to order: ")

    if order in menu:
            total = menu[order]
            print("total bill is",total)
            
    else:
        print("product not present, re-enter your product")
        product()

product()
