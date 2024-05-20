l1 = [int(x) for x in input("Enter the elements of the list: ").split()]
n = len(l1)
def find_min(l1,i,n):
    m = l1[i]
    pos = i   
    for j in range(i,n):
        if l1[j]<m:
            m = l1[j]   
            pos = j
    return pos
print(l1)
for i in range(n):
    pos = find_min(l1,i,n)
    l1[i],l1[pos] = l1[pos],l1[i]

print(l1)



