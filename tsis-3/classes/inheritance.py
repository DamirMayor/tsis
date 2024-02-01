#1
class Student(Person):


#2
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()


#Examples
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()
class Teacher(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Teacher("Mike", "Olsen")
x.printname()
class Studentnumbertwo(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
x = Studentnumbertwo("Mike", "Olsen")
x.printname()
print('\n')
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
x = Student("Mike", "Olsen")
print(x.graduationyear)
print('\n')
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
print('\n')
class Person:
  def __init__(self, fname, lname, year):
    self.fname = fname
    self.lname = lname
    self.year = year
  def welcome(self):
    print("Welcome", self.fname, self.lname, "to the class of", self.year)
x = Person("Damir", "Sag", 2012)
x.welcome()
