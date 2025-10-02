""" print("Helloee")
import sys
print(sys.version)
## hellp
x=5 
y="10"
print(x+y)   # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(x+int(y))  #15
print(str(x)+y)  #510
print(float(x)+float(y))  #15.0
print(type(x))  #<class 'int'>
print(type(y))  #<class 'str'>
# many values to multiple variables
a,b,c=5,10.5,"Hello"
print(a)  #5
print(b)  #10.5
print(c)  #Hello
#list to multiple variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) #apple
print(y) #banana
print(z) #cherry

"""
#global variable are any variable that is defined outside of a function and can be accessed inside a function
""" x = "awesome"   
def myfunc():
    print("Python is " + x)
myfunc()  #Python is awesome
#local variable are any variable that is defined inside a function and can only be accessed inside that function
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()  #Python is fantastic
print(x)  #awesome

#global keyword is used to create a global variable inside a function
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)  #Python is fantastic

 """
""" 
# data types
x = 5               # integer
y = 5.5             # float
z = 1j              # complex
a = "Hello"         # string
b = True            # boolean
c = ["apple", "banana", "cherry"]  # list
d = ("apple", "banana", "cherry")  # tuple
e = range(6)       # range
f = {"name": "John", "age": 36}  # dictionary
g = {"apple", "banana", "cherry"}  # set
h = frozenset({"apple", "banana", "cherry"})  # frozenset
i = bytes(5)       # bytes
j = bytearray(5)   # bytearray
k = memoryview(bytes(5))  # memoryview
z = None          # NoneType

#rando  m module
import random
print(random.randint(1,100))  # random integer between 1 and 100
print(random.random())  # random float between 0.0 and 1.0
print(random.choice(['apple', 'banana', 'cherry']))  # random choice from a list
print(random.sample(range(100), 5))  # random sample of 5 unique numbers
print(random.uniform(1, 10))  # random float between 1 and 10

 """
""" 
## Python strings

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print('''daskdhaska
ashkshakshksk
      asahdkahdka''') #multiline string or '''    '''


a = "Hello, World!"
print(a[1])        # e
print(a[2:5])      # llo

print(a[:5])       # Hello
print(a[2:])       # llo, World!
print(a[-5:-2])    # orl
print(a.replace("H", "J"))  #Jello, World!
print(a.split(","))  #['Hello', ' World!'] #returns ['Hello', ' World!'] as a list

for x in "banana":
  print(x) #prints each character in a new line

print(len(a))  #13 #length of string
print(a.lower())  #hello, world!
print(a.upper())  #HELLO, WORLD!

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")  #No, 'expensive' is NOT present.

#string concatenation
a = "Hello"
b = "World"
c = a + " " + b #Hello World
z = a + b     #HelloWorld

#string formatting
age = 36   
txt = "My name is John, and I am {}"  #My name is John, and I am 36
print(txt.format(age)) 
# or  
print(f"My name is John, and I am {age}")  #My name is John, and I am 36
# or
print("My name is John, and I am", age)  #My name is John, and I am 36

#escape characters
txt = "We are the so-called \"Vikings\" from the north."  #We are the so-called "Vikings" from the north.
print(txt)
txt = "Hello\nWorld!"  #Hello
                      #World!
print(txt)
txt = "Hello\tWorld!"  #Hello   World!
print(txt)
txt = "Hello\rWorld!"  #World! (overwrites "Hello")
print(txt)
txt = "Hello\bWorld!"  #HellWorld! (removes the character before \b)
print(txt)
txt = "Hello\\World!"  #Hello\World!
print(txt)
txt = "Hello\'World!"  #Hello'World!
print(txt)
txt = "Hello\"World!"  #Hello"World!
print(txt)
 """

