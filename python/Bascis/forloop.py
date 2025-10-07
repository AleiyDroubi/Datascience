fruits = ["apple", "banana", "cherry", "mango"]
for x in fruits:
    print(x)
for x in "banana":
    print(x) #prints each letter in banana

for i in fruits:
    print(i) #prints each fruit using index
    if i == "banana":
        break #exits the loop when it reaches banana

for i in fruits:
    if i == "banana":
        continue #skips the rest of the code and goes to next iteration
    print(i) #prints apple, cherry, mango

for i in range(6):
    print(i) #prints 0 to 5
for i in range(2, 6):
    print(i) #prints 2 to 5
for i in range(2, 30, 3):
    print(i) #prints 2 to 29 with a step of 3
else:
    print("Finally finished!") #executes after the loop is finished normally

#even numbers
for i in range(2, 30, 2):
    print(i) #prints even numbers from 2 to 28
#odd numbers
for i in range(1, 30, 2):
    print(i) #prints odd numbers from 1 to 29
#nested for loop
adj = ["red", "big", "tasty"]  
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
