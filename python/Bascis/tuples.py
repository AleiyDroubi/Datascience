thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(type(thistuple))
print(len(thistuple))
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])
print(thistuple[:2])
print(thistuple[1:])
print(thistuple[-3:-1])
a = ("apple", "banana", "cherry")
thistuple = tuple(a)
print(thistuple)
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
#tuple items are unchangeable, but we can convert it to a list and change then convert it back to tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#works for adding too and removing and other list methods
x = list(x)
x.append("orange")
x.remove("apple")
x = tuple(x)
print(x)
#but tuples have only two methods count and index
print(x.count("apple"))
print(x.index("cherry"))
#add two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#unpack a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#using asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits  
print(green)
print(yellow)
print(red)
#loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
for i in range(len(thistuple)):
    print(thistuple[i])