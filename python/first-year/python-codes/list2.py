menu=["burger",'pizza','sushi']
search=input("Enter menue item: ")
if search in menu:
    print("It's availbale")
else:
    print("Not found")

menu.append("choco")
print(menu)
print(menu.index("choco"))
menu.insert(4,"Dessert")
print(menu)
menu.reverse()
print(menu)
menu.remove("burger")
print(menu)
print(len(menu))
del menu[0]
print(menu)
x=menu
menu.append(3)
print(x)
print(menu)
print(menu[3])
print(x)
x.append(4)
print(menu)