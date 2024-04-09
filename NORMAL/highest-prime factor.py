num = int(input("Enter a number: "))
fact_list = []
prime = []
for i in range(1, num+1):
    if num %i== 0:
        fact_list.append(i)
print(fact_list)