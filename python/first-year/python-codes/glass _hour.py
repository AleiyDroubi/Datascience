n = int(input("Enter the number of rows:(MUST BE ODD) "))
while(n%2==0):
    n = int(input("Enter the number of rows:(MUST BE ODD) "))
    # for a reversed tree
for i in range( n ,0,-2):
    for k in range(n,i,-2):
        print(" ",end=(""))
    for j in range(i):
        print("*", end="")

    print("")
    # for a tree
for i in range( 1,n+1,2):
    for x in range(n,i,-2):
        print(" ",end=(""))
    for y in range(i):
        print("*", end="")
    print("")




