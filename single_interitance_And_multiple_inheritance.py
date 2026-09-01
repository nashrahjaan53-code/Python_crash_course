##single inheritance:

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self,name, breed):
        Animal.__init__ (self, name, species = "Dog")
        self.breed = breed
    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

##multiple_inheritance:

class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"The name  is{self.name}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

o = DancerEmployee("Roph", "Chinko")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())

