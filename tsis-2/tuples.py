#1
fruits = ("apple", "banana", "cherry")
print(fruits[0])


#2
fruits = ("apple", "banana", "cherry")
print(len(fruits))


#3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])


#4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


#Examples
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(type(thistuple))
thistuple = ("apple")
print(type(thistuple))
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
print(thistuple[1])
print(thistuple[-1])
print('\n')
x = ("rabbit", "fox", "wolf")
y = list(x)
y[1] = "kolobok"
x = tuple(y)
print(x)
y = ("elephant",)
x += y
print(x)
y = list(x)
y.remove("wolf")
x = tuple(y)
print(x)
(odin, dva, tri) = x
print(odin)
print(dva)
print(tri)
for y in x:
  print(y)
mytuple = x * 2
print(mytuple)
