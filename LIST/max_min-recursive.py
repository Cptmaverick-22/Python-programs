
l = [5,8,9,3,2]
max = l[0]
min = l[0]
for i in range(len(l)):
    if l[i]>=max:
        max = l[i]
    elif l[i]<=min:
        min = l[i]
print("Max element is: ",max)
print("Min element is: ",min)
