# Greatest of Two Numbers

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
    print("Greatest =", a)
else:
    print("Greatest =", b)


# Greatest of Three Numbers

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print("Greatest =", a)
elif b > c:
    print("Greatest =", b)
else:
    print("Greatest =", c)
