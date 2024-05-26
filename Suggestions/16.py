l1 = [int(x) for x in input("Enter the elements: ").split()]
n = len(l1)
print(l1)
for i in range(n):
    for j in range(0, n-1):
        if l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]

print("Sorted array is:", l1)
