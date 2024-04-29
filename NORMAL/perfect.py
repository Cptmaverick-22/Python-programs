fact = []
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if n % i == 0:
        fact.append(i)
fact.pop()
if sum(fact) == n:
    print("perfect number")
else:
    print("Not a prime number")
