n = int(input("Enter a number: "))
a = 0
b = 1
sum = 0
fibo_list = []
for i in range(n):
    fibo_list.append(a)
    a,b = b,a+b

print(fibo_list)

for x in fibo_list:
    if x%2==0:
        sum = sum+x
print("The sum of even numbers is: ",sum)