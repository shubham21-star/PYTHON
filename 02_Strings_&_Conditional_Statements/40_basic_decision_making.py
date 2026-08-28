# Check Positive / Negative / Zero

num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Login System

user = input("Username: ")
pwd = input("Password: ")

if user == "admin" and pwd == "1234":
    print("Access Granted")
else:
    print("Access Denied")

# Number Range Check
num = int(input("Enter number: "))

if num >= 1 and num <= 100:
    print("In range")
else:
    print("Out of range")

# ATM 

balance = 10000
amount = int(input("Enter amount: "))

if amount <= balance and amount % 100 == 0:
    print("Withdrawal successful")
else:
    print("Invalid request")
