#1
x = lambda a : a


#Examples
x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b, c : a + b + c
print(x(5, 6, 7))
print('\n')
def my_func(n):
  return lambda a : a * n
my_func1 = my_func(2)
print(my_func1(11))
