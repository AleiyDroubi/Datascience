n = int(input("Enter the number of rows: "))

for i in range( n ,0,-2):
    for k in range(n,i,-2):
        print(" ",end=(""))
    for j in range(i):
        print("*", end="")

    print("")
