input = input("Enter the numbers: ")
l = [int(x) for x in input.split()]
even = []
for i in l.copy():
    if i %2==0:
        even.append(i)
print(even)