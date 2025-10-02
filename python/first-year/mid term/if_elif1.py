package_price=99
package_purshased=int(input("Enter total package purshased: "))
def discount():
    if 10<=package_purshased<=19:
        print("You have 20%"" discount on the following purshase",total_price(.2))
    elif 20<=package_purshased<=49:
        print("You have 30%"" discount on the following purshase",total_price(.3))        
    elif 50<=package_purshased<=99:
        print("You have 40%"" discount on the following purshase",total_price(.4))
        
    elif package_purshased>=100:
        print("You have 50% discount on the purshase",total_price(.5))
    else:
        print("You have no discount",total_price(0))        
def total_price(x):
    total=package_price*package_purshased
    dis=total*x
    price=total-dis
    return price
discount()    