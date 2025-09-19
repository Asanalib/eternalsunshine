x = 5
y = "John"
print(x)
print(y)
print(type(x))
print(type(y))


a=str(3)
b=int(3)
c=float(3)

"""
Camel Case
Each word, except the first, starts with a capital letter:
"""

myVariableName = "John"


# Pascal Case
# Each word starts with a capital letter:

MyVariableName = "John"


# Snake Case
# Each word is separated by an underscore character:

my_variable_name = "John"



l, m, n = "Orange", "Banana", "Cherry"
print(l)
print(m)
print(n)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)







x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)