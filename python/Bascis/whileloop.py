i = 1
while i < 6:
    print(i)
    i += 1
#break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break #exits the loop
    i += 1
#continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue #skips the rest of the code and goes to next iteration
    print(i) #prints 1,2,4,5,6
#else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
