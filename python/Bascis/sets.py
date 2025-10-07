myset = {1, 2, 3, 4, 5}
print(myset)
print(type(myset))
print(len(myset))
print(3 in myset)
print(6 in myset)
myset.add(6)
print(myset)
myset.add(3)
print(myset)
myset.update([7, 8, 9])
print(myset)
#does not add duplicate 
myset.remove(3)
print(myset)
#throws error if item not found
#myset.remove(10)
myset.discard(10)
#does not throw error if item not found
print(myset)
myset.pop()
#removes a random item
print(myset)
#items cant be changed but we can add and remove items
myset.clear()
print(myset)
del myset
#print(myset)
#deletes the set

#accessing items through loop or in operator
myset = {1, 2, 3, 4, 5}
for x in myset:
    print(x)
print(3 in myset)
print(6 in myset)
#sets are unordered so we cant access items through indexing
#myset[0] #throws error
#Join two sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2) #returns a new set or we can use set1 | set2
print(set3)
set1.update(set2) #updates set1
print(set1)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.intersection(set2) #returns a new with common items in both sets
print(set3)
set1.intersection_update(set2) #updates the set1
print(set1)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.symmetric_difference(set2) #returns a new set with items not common in both sets
print(set3)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)
#difference or - 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.difference(set2) #returns a new set with items in set1 but not in set2
print(set3)