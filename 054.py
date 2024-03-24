# Inheritance in Python
# Class derived from another class inheriting the properties and methods of parent class is called inheritance

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of the employee is {self.name} ID is {self.id}")

e1 = Employee("Rohit",654)
e1.showDetails()
e2 = Employee("Mohit",852)
e2.showDetails()

class programmer(Employee):
    def showLanguage(self):
        print("Default language is Python")

e3 = programmer("Shrija",687)
e3.showLanguage()