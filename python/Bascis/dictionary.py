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

#filtering
thisdict = {
  "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
newdict = {k: v for k, v in thisdict.items() if k != "model"}
print(newdict)  #{'brand': 'Ford', 'year': 1964, 'colors': ['red', 'white', 'blue']}

sales_data ={
    "January": 1500,
    "February": 1800,
    "March": 1200,
    "April": 2000,
    "May": 1700
}
high_sales = {month: sales for month, sales in sales_data.items() if sales > 1600}
print(high_sales)  #{'February': 1800, 'April': 2000 'May': 1700}
low_sales = {month: sales for month, sales in sales_data.items() if sales <= 1600}
print(low_sales)  #{'January': 1500, 'March': 1200}

sorted_sales = dict(sorted(sales_data.items(), key=lambda item: item[1], reverse=True))
print(sorted_sales)  #{'April': 2000, 'February': 1800, 'May': 1700, 'January': 1500, 'March': 1200}