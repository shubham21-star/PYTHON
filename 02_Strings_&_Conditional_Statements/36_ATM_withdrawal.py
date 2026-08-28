balance = 10000
amount = int(input("Enter amount: "))

if amount <= balance and amount % 100 == 0:
    print("Withdrawal successful")
else:
    print("Invalid request")

# with minimum balance

balance = 10000
min_balance = 500

amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount % 100 != 0:
    print("Amount must be multiple of 100")
elif balance - amount < min_balance:
    print("Insufficient balance")
else:
    balance -= amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)
