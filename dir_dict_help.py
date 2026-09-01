#dir, __dict__, help method in python:

#1.dir:
x = (1,2,3)
print(dir(x))
print(x.__add__)

##__dict__:
class Person:
    def __init__ (self, name,age):
        self.name = name
        self.age=age

p = Person("Chinko", 2)
print(p.__dict__)


##Help:
print(help(str))
