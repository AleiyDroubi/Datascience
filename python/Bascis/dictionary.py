thisdict = {
  "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))
print(len(thisdict))
print(thisdict["brand"])
print(thisdict.get("model"))
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
thisdict["year"] = 2020
print(thisdict)

#change or add item
thisdict["color"] = "black"
print(thisdict)
thisdict.update({"year": 2021, "color": "green"})
print(thisdict)
#remove item
thisdict.pop("model")
print(thisdict)
thisdict.popitem() #removes last inserted item
print(thisdict)
del thisdict["brand"]
print(thisdict)
#del thisdict #deletes the dictionary
#print(thisdict)
thisdict.clear() #empties the dictionary
print(thisdict)
#loop through a dictionary
thisdict = {
  "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
for x in thisdict:
    print(x) #prints keys
for x in thisdict.keys():
    print(x) #prints keys
for x in thisdict:
    print(thisdict[x]) #prints values
for x in thisdict.values():
    print(x) #prints values
for x, y in thisdict.items():
    print(x, y) #prints key and value
#copy a dictionary
mydict = thisdict.copy()
print(mydict)
mydict = dict(thisdict)
print(mydict)
#nested dictionary
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}
print(myfamily)
print(type(myfamily))
print(len(myfamily))
print(myfamily["child1"])
print(myfamily["child1"]["name"])
#loop through nested dictionary
for x, y in myfamily.items():
    print(x)
    for i, j in y.items():
        print(i, j)
