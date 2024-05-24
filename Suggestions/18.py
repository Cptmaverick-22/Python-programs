balance = 0
while True:
    choice = input("What would you like to do: 'Deposit', 'Withdraw', 'Check Net Amount' or 'Quit': ")

    if choice.lower() == 'deposit':
        amount = int(input("Enter the amount you want to deposit: "))
        balance += amount

    elif choice.lower() == "withdraw":
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient funds. Withdrawal failed.")

    elif choice.lower() == 'check net amount':
        print("The net amount is:", balance)

    elif choice.lower() == 'quit':
        exit()
        
    else:
        print("Wrong choice, enter the choice again")