start = int(input("Enter start range: "))
end = int(input("Enter end range: "))
num = int(input("Enter number to check: "))

if start > end:
    print("Invalid range")
elif start <= num <= end:
    print("Number is in range")
else:
    print("Number is out of range")
