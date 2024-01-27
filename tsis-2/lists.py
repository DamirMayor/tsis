#1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])


#2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"


#3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")


#4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")


#5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")


#6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])


#7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


#8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


#Examples
list = ["aboba", "biba", "boba", "aboba", "boba"]
print(list)
print(len(list))
print('\n')
list1 = ["car", "bike", "shoes"]
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, True]
list4 = [False, "print_name", 14, True, "Damir", 18]
print('\n')
mylist = ["Python", "Java", "CPP", "HTML"]
print(type(mylist))
print('\n')
shoes = list(("sneakers", "moccasins"))
print(shoes)
print('\n')
print(list[1])
print(list[-1])
print(list[1:4])
print(list[:4])
print(list[2:])
print('\n')
thislist = ["apple", "banana", "cherry", "apple"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
thislist[1] = "blackcurrant"
print(thislist)
thislist[1:2] = ["melon", "watermelon"]
print(thislist)
thislist.append("orange")
print(thislist)
thislist.insert(3, "orange")
print(thislist)
thislist.remove("apple")
print(thislist)
thislist.pop(1)
print(thislist)
del thislist[0]
print(thislist)
del thislist
print('\n')
thislist = ["Tomato", "potato", "cucumber", "Onion", "pumpkin", "cubbage"]
for x in thislist:
  print(x)
for i in range(len(thislist)):
  print(thislist[i])
j = 0
while j < len(thislist):
  print(thislist[j])
  j += 1
[print(x) for x in thislist]
newlist = []
for x in thislist:
  if "o" in x:
    newlist.append(x)
print(newlist)
del newlist
newlist = [x for x in thislist if "o" in x]
print(thislist)
newlist1 = [x.upper() for x in thislist]
print(newlist1)
print('\n')
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)
del thislist
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
newlist.sort(key = str.lower)
print(newlist)
thislist.reverse()
print(thislist)
print('\n')
del mylist
mylist = ["Toyota", "Volvo", "Geely", "Porsche"]
mylist1 = mylist.copy()
print(mylist1)
mylist2 = list(mylist)
print(mylist2)
print('\n')
lista = ["a", "b", "c"]
listb = [1, 2, 3]
listc = lista + listb
print(listc)
for x in listb:
  lista.append(x)
print(lista)
del lista
del listb
del listc
lista = ["a", "b", "c"]
listb = [1, 2, 3]
lista.extend(listb)
print(lista)
y = lista.count("a")
print(y)
lista.clear()
index = listb.index(2)
print(index)
