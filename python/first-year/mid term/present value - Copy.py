f=float(input("Enter future value:"))
r=float(input("Enter rate of interst:"))
n=float(input("Number of years:"))
p=f/(1+r)**n
print("you need to deposit:",round(p,3))
