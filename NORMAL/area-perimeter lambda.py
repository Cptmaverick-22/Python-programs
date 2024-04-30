length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))

area = lambda l,b : l*b
perimeter = lambda l,b : 2*(l+b)
print(f"the area of {length} and {breadth}: {area(length,breadth)} and the perimeter of {length} and {breadth} is: {perimeter(length,breadth)}")