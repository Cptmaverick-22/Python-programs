def merge1(a,p,q,r):
    left=[]
    right=[]
    n1=q-p+1
    n2=r-q
    for i in range(n1+1):
        x=a[p+i]
        left.append(x)
    for j in range(n2):
        y=a[q+j+1]
        right.append(y)
    left.append(99999)
    right.append(99999)
    i=0
    j=0
    for k in range(p,r+1):
        if left[i]<=right[j]:
            a[k]=left[i]
            i=i+1
        else:
            a[k]=right[j]
            j=j+1
def merge_sort1(a,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort1(a,p,q)
        merge_sort1(a,q+1,r)
        merge1(a,p,q,r)

a=[int(x) for x in input("Enter the elements in the list: ").split()]
n = len(a)
print("unsortrd array: ",a)
p=0
r=n-1
merge_sort1(a,p,r)
print("unsortrd array: ", a)