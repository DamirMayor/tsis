#1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))


#2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020


#3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"


#4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")


#5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()


#Examples
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(thisdict.get("model"))
x = thisdict["model"]
print(x)
x = thisdict.keys()
print(x)
thisdict["color"] = "white"
print(x)
x = thisdict.values()
print(x)
x = thisdict.items()
print(x)
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
thisdict.update({"year": 2020})
print(thisdict)
thisdict.update({"color": "red"})
print(thisdict)
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
for x in thisdict:
  print(x)
for x in thisdict.values():
  print(x)
for x in thisdict.keys():
  print(x) 
for x, y in thisdict.items():
  print(x, y) 
mydict = thisdict.copy()
print(mydict) 
mydict = dict(thisdict)
print(mydict)
print('\n')
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print(myfamily["child2"]["name"])
print('\n')
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
print('\n')
x = ('key1', 'key2', 'key3')
y = ('value1', 'value2', 'value3')
thisdict = dict.fromkeys(x, y)
print(thisdict)
print('\n')
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
print('\n')
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "White")
print(x)
