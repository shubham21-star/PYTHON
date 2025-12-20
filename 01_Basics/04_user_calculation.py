#  write a program to solve given mathematical equation

s= int(input("Enter number (s):  "))
a= int(input("Enter number (a):  "))
b= int(input("Enter number (b):  "))
c= int(input("Enter number (c):  "))

print((s*((s-a)+(s-b)+(s-c)))**1/2)