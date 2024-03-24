# Static Method in Python
# this method is defined using @staticmethod decorator
class Math:
    def __init__(self,num):
        self.n = num

    def addtonum(self,n):
        self.n = self.n + n

    @staticmethod
    def add(a,b):
        return(a+b)

obj = Math(3)
print(obj.n)
obj.addtonum(6)
print(obj.n)
print(Math.add(9,3))