num = int(input("Enter a number: "))
fact_list = []
prime = []
for i in range(1, num+1):
    if num %i== 0:
        fact_list.append(i)
print(fact_list)
for n in fact_list:
    if n > 1:
        for j in range(2,n):
            if n % j == 0:
                break
        else:
            prime.append(n)
print(prime)