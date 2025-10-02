ans="Y"
num=list(range(1,11))
lettr=['i','ii','iii','iv','v','vi','vii','viii','ix','x']

while ans=="y" or ans=="Y":
    num1=int(input("number= "))
    while num1<1 or num1>10:
        print("Invalid number")
        num1=int(input("number= "))
    index=num.index(num1)

    print("Number in romamian is: ")
    print("----------------")
    print(num1,'\t',lettr[index])
    print("----------------")
    ans=input("Enter 'y' to try again ") 
