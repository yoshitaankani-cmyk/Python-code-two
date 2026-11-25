
balance = float(input("Enter initial balance: "))
n = int(input("Enter number of transactions: "))

deposits = 0
withdrawals = 0

for i in range(n):
    print("\nTransaction", i + 1)
    print("1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter your choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")

    elif choice == 1:
        balance = balance + amount
        deposits = deposits + amount
        print("Deposit successful")

    elif choice == 2:
        if amount <= balance:
            balance = balance - amount
            withdrawals = withdrawals + amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    else:
        print("Invalid transaction")

print("\n----- ATM SUMMARY -----")
print("Total deposits:", deposits)
print("Total withdrawals:", withdrawals)
print("Final balance:", balance)
