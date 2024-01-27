#1 
print(10>9)
#True


#2
print(10==9)
#False


#3
print(10 < 9)
#False


#4
print(bool("abc"))
#True


#5
print(bool(0))
#False


#Examples
print(15 == 7)
print(15 > 7)
print(15 < 7)
print(bool(23))
print(bool(0))
print('\n')
a = 20
b = 78
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print('\n')
"""The following will return False"""
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
print('\n')
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
print('\n')
def myFunction() :
  return True
print(myFunction())
print('\n')
x = 476.0
print(isinstance(x, float))
