num = int(input("Enter a number: "))
fact_list = []

for i in range(1, num+1):
    if num %i== 0:
        fact_list.append(i)
print(fact_list)
prime = [n for n in fact_list if n > 1 and all(n % j != 0 for j in range(2, int(n**0.5) + 1))]
print(max(prime))
