l1 = [int(i) for i in input("Enter the number of elements: ").split()]
l2 = [int(i) for i in input("Enter the number of elements: ").split()]
print("common elements are: ", list(filter(lambda x: x in l2,l1)))