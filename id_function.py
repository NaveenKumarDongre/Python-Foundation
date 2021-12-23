# id() method in python

print(id(5))

a = 10

print(id(a))

b = a

print(id(b))

""" here basically we will see 
that id(a) is equal to id(b) as both
a and b are refering to the same object
integer which is 10
"""

a = 10
b = 10
print(id(a))
print(id(b))
""" here basically we will see 
that id(a) is equal to id(b) as both
a and b are refering to the 10 which is basically
a literal in python literal are stored at a 
particular memory space and this variable "a"
and "b" are just the references to the memory 
location where 10 is stored.

"""
