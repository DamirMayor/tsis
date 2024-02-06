#1
def my_function():
  print("Hello from a function")


#2
def my_function():
  print("Hello from a function")

my_function()


#3
def my_function(fname, lname):
  print(fname)


#4
def my_function(x):
  return x + 5


#5
def my_function(*kids):
  print("The youngest child is " + kids[2])


#6
def my_function(**kid):
  print("His last name is " + kid["lname"])


#Examples
def my_function(fname):
  print(fname + " Kardashyan")
my_function("Kim")
my_function("Jenna")
my_function("Ortega")
print('\n')
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")
print('\n')
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
print('\n')
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
print('\n')
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print('\n')
def my_function(x, /):
  print(x)
my_function(3)
print('\n')
def my_function(x):
  print(x)
my_function(x = 3)
print('\n')
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)
