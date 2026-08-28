#  parking lot that charges customers

T_earning = 0

for i in range(1,11):
    hours = int(input(f"Enter Your Parking Duration {i}:"))

    if (hours <=1) :
        cost = 5
    else:
        cost = 5 + (hours -1)*3
    T_earning += cost

print("\n=====PARKING MANAGMENT SYSTEM=====")
print("Total Cost of Parking:", T_earning)
print("==================================")