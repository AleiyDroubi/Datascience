a = 10
b = 20
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")
#nested if
a = 10
b = 20
c = 30
if a > b:
    print("a is greater than b")
elif b > c:
    print("b is greater than c")
else:
    print("c is greatest")
#short hand if else
a = 10
b = 20
if a > b:print("a is greater than b")  
else:print("b is greater than a")
#short hand if
print("a is greater than b") if a > b else print("b is greater than a")

#and or not
a = 10  
b = 20
c = 30
if a > b and c > a:
    print("Both conditions are true")
if a > b or a < c:
    print("At least one of the conditions is true")
if not a > b:
    print("a is not greater than b")

#nested if
x = 1
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
else:
    print("Below 10.")
#pass statement
a = 10
b = 20  
if b > a:
    pass #does nothing

#match case (like switch case in other languages)
x = 2
match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Something else")
#the default case is written as case _