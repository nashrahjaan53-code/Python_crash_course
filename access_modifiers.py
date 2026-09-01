#access modifiers: are not in python but we use it for our conveince
class Employee:
    def __init__(self):
        self.__name = "Nashrah"
    
a = Employee()
#print(a.__name) ## cannot be accessed directly
print(a._Employee__name)

## types:
#public
#2. private
#3. protected

## private one is used b putting double underscore
## to access a private varibale:
## name mangling 

## protected::
class Student:
    def __int__(self):
        self._name = "Nashrah"

    def _funName(self): # protected method
        return "Hey there welcome!"
class Subject(Student):
    pass

obj = Student()
obj1 = Subject()

print(obj ._name)
print(obj ._funName())
print(obj1 ._name)
print(obj1 ._funName())
