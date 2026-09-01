##inheritance:
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of the Employee : {self.id} is {self.name}")
class Programmer(Employee):
    def show_language(self):
        print("The default language is python")
        
e1 = Employee("Chinko", 400)
e1.showDetails()
e2 = Programmer("Nashrah", 4100)
e2.showDetails()
e2.show_language()
