#1
class MyClass:
  x = 5

  
#2
class MyClass:
  x = 5

p1 = MyClass()


#3
class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)


#4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


#Examples
class MyClass:
  x = 5
print(MyClass)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print('\n')
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name} {self.age}"    
p1 = Person("John", 36)
print(p1)
print('\n')
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()
print('\n')
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(mysillyobject):
    print("Hello my name is" + mysillyobject.name)
  p1 = Person("John", 36)
  p1.myfunc()
  p1.age = 40
  print(p1.age)
  del p1
