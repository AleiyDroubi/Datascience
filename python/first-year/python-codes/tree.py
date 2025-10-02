n = int(input("Enter the number of rows: "))


for col_row in range( 1,n+1,2):
    for x in range(n,col_row,-2):
        print(" ",end=(""))
    for y in range(col_row):
        print("*", end="")
    print("")
