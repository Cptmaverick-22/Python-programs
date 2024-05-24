l1 = [2 ,5 ,8,9,1,0]
input = int(input("Enter the element you want to search: "))
for i in range(0,len(l1)):
    if l1[i] == input:
        print("Element is present at location: ",i)
        break
else:
    print("not prsent")