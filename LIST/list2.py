l1 = [1,2,38,34,78,45,32,12,9]
key = int(input("Enter the number: "))
for i in l1:
    if i == key:
        print("Element is present at location",l1[i])
        break
else:
    print("Element is no present")
    

