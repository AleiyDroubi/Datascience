import pandas as pd
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

""" print(myvar)
 """

a =[1,2,3,4,5]
myvar2 = pd.Series(a)
print(myvar2)
print(myvar2[0])
print(myvar2[1])
print(myvar2[2:4])  # slicing similar to lists
print(myvar2[0:4])  # slicing similar to lists

b = [7,8,9,10]
myvar3 = pd.Series(b, index = ["a", "b", "c", "d"])
print(myvar3)
print(myvar3["a"])
print(myvar3["b"])
print(myvar3["c":"d"])  # slicing similar to lists
print(myvar3["a":"c"])  # slicing similar to lists


calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)