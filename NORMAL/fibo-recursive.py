n = int(input("Enter a number: "))
def fibo(n):
    if (n<2):
        return n
    else:
        return fibo(n-2) + fibo(n-1)
    
for i in range(n):
    print(fibo(i))