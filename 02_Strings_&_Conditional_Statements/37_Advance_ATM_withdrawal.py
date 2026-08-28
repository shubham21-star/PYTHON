# ATM WITH DAILY LIMIT 

balance = 10000
min_balance = 500
daily_limit = 5000

amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount > daily_limit:
    print("Daily limit exceeded")
elif amount % 100 != 0:
    print("Amount must be multiple of 100")
elif balance - amount < min_balance:
    print("Insufficient balance")
else:
    balance -= amount
    print("Transaction successful")
    print("Remaining balance:", balance)
