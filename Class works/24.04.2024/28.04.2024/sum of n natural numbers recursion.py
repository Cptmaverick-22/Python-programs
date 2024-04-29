def sum_rec(n):
    if n<=1:
        return n
    else:
        return(n)+sum_rec(n-1)
    
n = int(input("Enter the number: "))
print(sum_rec(n))