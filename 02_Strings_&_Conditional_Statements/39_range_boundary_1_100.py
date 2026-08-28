num = int(input("Enter number: "))

if 1 <= num <= 100:
    print("Valid input")
elif num < 1:
    print("Below minimum range")
else:
    print("Above maximum range")
