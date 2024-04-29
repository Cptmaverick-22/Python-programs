num = int(input("Ente the integer: "))
count = 0
while num > 0:
    num = num&(num-1)
    count+=1
print(count)