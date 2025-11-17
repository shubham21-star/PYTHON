# input two variable
a = int(input("Enter first number (a):  "))
b = int(input("Enter second number (b):  "))

#display the original values
print(f"Before swapping: a = {a}, b = {b}")

# Swapping using temporary variable
temp = a
a = b
b = temp
#display the swapping values
print(f"After swapping: a ={a},b={b}")
#write a python programe to convert kilometers to miles
km = float(input("Enter distance in kilometers: ")) 
miles = km * 0.621371
print(f"{km} kilometers is equal to {miles} miles")
