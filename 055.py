# Access Specifiers/ Modifiers
# Limiting the access of variables, methods outside the class is done by access specifiers/ modifiers
# Public access specifiers: all default methods and variables are public

class student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
obj = student("Tom", 22)
print(obj.age)
print(obj.name)


# Private access specifiers: use "__" to make private access specifier 

class student:
    def __init__(self,name, age):
        self.__age = age # Making Private access modifier as variable
    def __funName(self): #  Making Private access modifier as method
        self.y = 56
        print(self.y)

class subject(student):
    pass
obj = student("Tom", 22)
obj1 = subject
# print(obj.__age)  # Calling Private access modifier as variable throws error
# print(obj1.__funName())  # Calling Private access modifier as method throws error

# Name Mangling
print(obj._student__age)  # Calling Private access modifier as variable using Name Mangling
print(obj._student__funName())  # Calling Private access modifier as method using Name Mangling


# Protected access specifiers: Protected specifier is just a writing convetion actually it do not provide any proction to element
class student:
    def __init__(self):
        self._name = "Tom" # Making Protected access modifier as variable
    def _funName(self): #  Making Protected access modifier as method
        return("Tom rocks")

class subject(student):
    pass
obj = student()
obj1 = subject()

print(obj._name)
print(obj._funName())
print(obj1._name)
print(obj1._funName())
