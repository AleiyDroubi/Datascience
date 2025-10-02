import random
def add(a,z=1):
    return(a+z)
for i in range(10):
    x = random.choices(("a",'B',"c","d"))
    print(x)

print(add(2,3))
print(add(2))