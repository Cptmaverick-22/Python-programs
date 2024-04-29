def linear_rec(n,l,key):
    if n==0:
        return -1
    elif l[n-1]==key:
            return (n-1)
    else:
        return(linear_rec(n-1,l,key))
    
l = [5,25,15,50,10,7]
n = len(l)
key = 15
index = linear_rec(n,l,key)
if index == -1:
    print("absent")
else:
    print("present",index)