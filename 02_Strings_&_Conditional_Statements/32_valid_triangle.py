a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
