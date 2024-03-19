# Python Class and Objects 

# class Details:
#     name = "Raman"
#     age = 23
#     prof = "Developer"
#     def sen(self):
#         print(self.name, "is a", self.prof)

# a = Details()
# print(a.name)
# print(a.prof)
# a.name = "Suraj"
# a.prof = "Tester"
# a.sen()

class people:
    name = "Jack"
    age = 22
    income = 10
    def info(self):
        print(f"{self.name} is of {self.age} age")

a = people()  # While assigning class to a variable "()" is must
b = people()
c = people()

a.name = "Ratan"
b.name = "Shaman"

a.age = 20
b.age = 24

a.info() # Also while calling a fuction of a class "()" is must 
b.info()
c.info()


