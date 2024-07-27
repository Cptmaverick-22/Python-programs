l1 = [int(x) for x in input("Enter the numbers: ").split()]
choice = int(input("Enter the element: "))
n = len(l1)
up = n-1
lb = 0
while lb <= up:
    mid = (lb+up)//2
    if l1[mid] == choice:
        print("Element found at location: ",mid)
        break
    elif l1[mid] > choice:
        up = mid - 1
    else:
        lb = mid + 1
else: 
    print("Element not found in the array")

