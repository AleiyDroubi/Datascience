def main():
    get_sum()
    get_sub()
    multiply()
    divide()


def get_sum ():
    print("Sum")
    print("")
    x=float(input("x="))
    y=float(input("y="))
    z=(x+y)
    print("sum=", z) 


def get_sub():
    print("") 
    print("Sub")
    x=float(input("x="))
    y=float(input("y="))
    z=(x-y)
    print("sub=",z) 
    

def multiply():
    print("")
    print("Mlutiplication")
    x=float(input("x="))
    y=float(input("y="))
    z=(x*y)
    print("multiply=", z) 


def divide():
    print("")
    print("Division")
    x=float(input("x="))
    y=float(input("y="))
    z=(x/y)
    print("division=", z)
main()

