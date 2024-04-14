def area(length,breadth):
    return length * breadth
def perimeter(length,breadth):
    return 2*(length + breadth)

length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))

print("Area is: ",area(length,breadth))
print("Perimeter is: ",perimeter(length,breadth))
