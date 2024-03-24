# Constructor or __init__() method in python:
class Details:
  def __init__(self): # Default Constructor
    print("animal Crab belongs to Crustaceans group")

obj1 = Details()

class Person:
    print("This is information about animal and its group")
    def __init__(self, animal, group): # Parameterized constructor
        self.ani = animal
        self.gro = group

    def info(self):
        print(f"{self.ani} belongs to {self.gro} group")

a = Person("Crab", "Crustacean")
b = Person("Fish","Pisces")
c = Person("Ostrich","Birds")
a.info()
b.info()
c.info()
