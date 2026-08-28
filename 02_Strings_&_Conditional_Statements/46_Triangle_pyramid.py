#code 1
n = int(input(("Enter No. of Row: ")))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(1,i+1):
        print("* ", end="")
    print()

#code 2

for i in range(1,n+1):
    for j in range(n-i):
        print("", end=" ")
    for k in range(1,2*i):
        print("*", end="")
    print()
print() 