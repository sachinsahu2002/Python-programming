# Getters and Setters
class funclass:
    def __init__(self,value): # Constructor
        self.val = value # assigning value

    def info(self): # Method 
        print(f"Value of the function is {self.val}") 
    
    @property # Getter 
    def value(self):
        return(10*self.val)
    
    @value.setter # Setter 
    def value(self,new_value):
        self.val = new_value
    
obj = funclass(20) # Creating an instance of a class i.e. is an object
print(obj.value) # Getting the value
obj.val = 10 # Setting the value
print(obj.value) # Again getting te value 
obj.info() # Calling a method of class


