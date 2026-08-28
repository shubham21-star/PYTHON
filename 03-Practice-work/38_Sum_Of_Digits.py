# 38_Sum_Of_Digits.py

n = int(input("Enter a number: "))
sum = 0
temp = n

while temp != 0:
    sum += temp % 10
    temp //= 10

print("Name: Shubham Kumar")
print("Sum of digits =", sum)
print("Name: Shubham Kumar")
