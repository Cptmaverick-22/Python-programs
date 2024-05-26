dep = [200,300,100,100]
withdraw = [150,150]
net_amount = sum(dep)-sum(withdraw)
print(net_amount)

#Another Way

transaction = [("Deposit",200),("Withdraw",150),("Deposit",300),("Withdraw",150),("Deposit",100),("Deposit",100)]

net_amount = 0

for i in transaction:
    type,amount = i
    if type == "Deposit":
        net_amount+=amount
    elif type == "Withdraw":
        net_amount-=amount

print(net_amount)
