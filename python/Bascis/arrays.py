car = ["BMW", "Volvo", "Ford"]
print(car)
print(type(car))  #<class 'list'>
print(len(car))   #3
print(car[0])     #BMW
print(car[-1])    #Ford
print(car[1:3])   #['Volvo', 'Ford']
print(car[:2])    #['BMW', 'Volvo']
print(car[1:])    #['Volvo', 'Ford']
print(car[-3:-1]) #['BMW', 'Volvo']
a = ["BMW", "Volvo", "Ford"]
car = list(a)
print(car)

import array as arr
a = arr.array('i', [1, 2, 3])
print(a)  #array('i', [1, 2, 3])
print(type(a))  #<class 'array.array'>
# array is for numbers only