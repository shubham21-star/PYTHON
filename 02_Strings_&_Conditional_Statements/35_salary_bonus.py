salary = int(input("Enter salary: "))
years = int(input("Years of service: "))

if years > 5:
    print("Bonus =", salary * 0.05)
else:
    print("No bonus")
