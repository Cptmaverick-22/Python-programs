def largest_smallest(num1,num2,num3):

    largest = num1
    smallest = num1

    if num2 > largest:
        largest = num2
    elif num2 < smallest:
        smallest = num2
    
    if num3 > largest:
        largest = num3
    elif num3 < smallest:
        smallest = num3

    return largest, smallest  

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

largest, smallest = largest_smallest(num1,num2,num3)
print("The largest number is: ",largest)
print("The smallest number is: ",smallest)
