units = int(input("Enter units: "))

if units <= 100:
    bill = units * 2
elif units <= 300:
    bill = 100 * 2 + (units - 100) * 3
else:
    bill = 100 * 2 + 200 * 3 + (units - 300) * 5

print("Bill =", bill)
