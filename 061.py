# Class as an Alternative constructor

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

e1 = Employee("Suman", 10000)
print(e1.name)
print(e1.salary)

string = "John-12000"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)

# Another example

# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     @classmethod
#     def square(cls,side):
#         return cls(side,side)
    
# rectangle1 = Rectangle(12,10)
# rectangle2 = Rectangle.square(10)
# print(rectangle1.width)
# print(rectangle1.height)
# print(rectangle2.width)
# print(rectangle2.height)
