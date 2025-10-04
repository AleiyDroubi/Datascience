#list
thislist = ["apple", "banana", "cherry"]
print(thislist)  #['apple', 'banana', 'cherry']
print(len(thislist))  #3
#A list with strings, integers and boolean values:
list1 = ["abc", 34, True]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = [1, "abc", 3.14, True]
print(type(thislist))  #<class 'list'>

tuple1 = ("apple", "banana", "cherry")
print(tuple1)  #('apple', 'banana', 'cherry')  
print(type(tuple1))  #<class 'tuple'>
tuple1 = list(tuple1)  #convert tuple to list
print(type(tuple1))  #<class 'list'>
print(tuple1)  #['apple', 'banana', 'cherry']
# accessing list items
print(thislist[1])  #banana
print(thislist[-1])  #cherry
print(thislist[1:3])  #['banana', 'cherry']
print(thislist[:3])  #['apple', 'banana', 'cherry']
print(thislist[1:])  #['banana', 'cherry']
#check if item exists
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")  #Yes, 'apple' is in the fruits list
#change item value
thislist[1] = "blackcurrant"
print(thislist)  #['apple', 'blackcurrant', 'cherry']
thislist[1:3] = ["watermelon", "kiwi"] # youc can replace multiple items withe single value
print(thislist)  #['apple', 'watermelon', 'kiwi']

#insert item
thislist.insert(2, "orange")
print(thislist)  #['apple', 'watermelon', 'orange', 'kiwi']
thislist.append("mango")
print(thislist)  #['apple', 'watermelon', 'orange', 'kiwi', 'mango']
thislist.extend(["pineapple", "papaya"])
print(thislist)  #['apple', 'watermelon', 'orange', 'kiwi', 'mango', 'pineapple', 'papaya']
#eextend can add any iterable object (tuples, sets, dictionaries etc.)
thislist2 = ['grapes', 'peach']
thislist.extend(thislist2)
print(thislist)  #['apple', 'watermelon', 'orange', 'kiwi', 'mango', 'pineapple', 'papaya', 'grapes', 'peach']
#remove item
thislist.remove("kiwi")
print(thislist)  #['apple', 'watermelon', 'orange', 'mango', 'pineapple', 'papaya', 'grapes', 'peach']
thislist.pop()  #removes last item
print(thislist)  #['apple', 'watermelon', 'orange', 'mango', 'pineapple', 'papaya', 'grapes']
thislist.pop(1)  #removes item at index 1
print(thislist)  #['apple', 'orange', 'mango', 'pineapple', 'papaya', 'grapes']
del thislist[0]  #removes item at index 0
print(thislist)  #['orange', 'mango', 'pineapple', 'papaya', 'grapes']
del thislist  #deletes the entire list
#print(thislist)  #this will raise an error because the list no longer exists
thislist = ["apple", "banana", "cherry"]
thislist.clear()  #empties the list
print(thislist)  #[]
#loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
for i in range(len(thislist)):
    print(thislist[i])
#while loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
#list comprehension
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in thislist:
    if "a" in x:
        newlist.append(x)
print(newlist)  #['apple', 'banana', 'mango']
newlist = [x for x in thislist if "a" in x]
print(newlist)  #['apple', 'banana', 'mango']

#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #sorts the list alphabetically
print(thislist)  #['banana', 'kiwi', 'mango', 'orange', 'pineapple']
thislist.sort(reverse=True) #sorts the list in descending order alphabetically
print(thislist)  #['pineapple', 'orange', 'mango', 'kiwi', 'banana']
thislist = [100, 50, 65, 82, 23]
thislist.sort() #sorts the list in ascending order
print(thislist)  #[23, 50, 65, 82, 100]
thislist.sort(reverse=True) #sorts the list in descending order
print(thislist)  #[100, 82, 65, 50, 23]

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)  #['apple', 'banana', 'cherry']
mylist = list(thislist)
print(mylist)  #['apple', 'banana', 'cherry']
#it can be done using slicing also :
mylist = thislist[:]
print(mylist)  #['apple', 'banana', 'cherry']
#join two lists
list1 = ["a", "b", "c"] 
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  #['a', 'b', 'c', 1, 2, 3]
list1.extend(list2)
print(list1)  #['a', 'b', 'c', 1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)  #['a', 'b', 'c', 1, 2, 3, 1, 2, 3]
list1 = ["a", "b", "c"] 
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  #['a', 'b', 'c', 1, 2, 3]