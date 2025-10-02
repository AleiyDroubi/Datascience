def main():
    sum=0
    x=int(input("Enter +ve number:"))
    while (x>0):
        sum+=x
        x=int(input("Enter +ve number, to stop enter a negative value: "))

    print("sum of numbers are:",sum)
main()
        