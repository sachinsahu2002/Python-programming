# Python Class methods

class Employee:
    company = "Google"
    def showinfo(self):
        print(f"The name is {self.name} and the company is {self.company}")

    @classmethod
    def change_company(cls,newcompany):
        cls.company = newcompany

e1 = Employee()
e1.name = "Jack"
e1.showinfo()
e1.change_company("Apple")
e1.showinfo()
print(Employee.company)
