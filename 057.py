# Class Variable Vs Instance variable
class Employee:
    noOfEmployee = 0 # Class variable
    companyName = "Fametrust" # Class variable
    def __init__(self, name):
        self.name = name # Instance Variable
        self.raise_amount = 0.02 # Instance Variable
        Employee.noOfEmployee += 1 # Modifing class variable using Instance

    def show_details(self):
        print(f"The name of the employee is {self.name} and raise of {self.noOfEmployee} seized {self.companyName} company is {self.raise_amount}")

emp1 = Employee("Ram")
emp1.comapanyName = "Goindia"
emp1.raise_amount = 0.3
emp1.show_details()


emp2 = Employee("Prateek")
emp2.comapanyName = "Indus"
emp2.show_details()

emp3 = Employee("karan")
emp4 = Employee("Devika")
emp5 = Employee("Suresh")
emp6 = Employee("harshita")

emp3.companyName = "Yamaha"
emp4.companyName = "Googler"
emp5.companyName = "indisweat"
emp6.companyName = "Gojack"

emp3.show_details()
emp4.show_details()
emp5.show_details()
emp6.show_details()