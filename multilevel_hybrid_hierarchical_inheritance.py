##multilevel inheritance:
class Animal:
    def __init__(self, name,species):
        self.name = name
        self.species = species
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name,species = "Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self,name,color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o = GoldenRetriever("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())


##example of hybrid inheritance:
class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass
class Derived3(Derived1, Derived2):
    pass

##hierarchical inheritance:
#CEO
  #|
#----
 #Manager
 # |
#----
#Employee

class BaseClass:
    pass
class D1 (BaseClass):
    pass
class D2(BaseClass):
    pass
class D3(D1):
    pass
