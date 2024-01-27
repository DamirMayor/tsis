#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")


#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")


#3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)


#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")


#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


#Examples
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
myset = {"apple", "banana", "cherry"}
print(type(myset))
for x in thisset:
  print(x)
print("banana" in thisset)
thisset.add("orange")
print(thisset)
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
thisset.remove("banana")
print(thisset)
thisset.discard("banana")
print(thisset)
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal
thisset.clear()
print(thisset)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) 
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
