def area(length,breadth):
    return length * breadth
def perimeter(length,breadth):
    return 2*(length + breadth)

length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))

Area = area(length,breadth)
Perimeter = perimeter(length,breadth)

print("Area is: ",Area)
print("Perimeter is: ",Perimeter)
