# Local and Global Variable in Python

x = 1235 # Global variable
y = 5 # Global variable
 
def myfun():
    x = 34 # local variable
    global y # This changes global y (NOT RECOMMENDED)
    if x%y == 0:
        print("Cool")
        print(x)
    else:
        print("Hot")
        print(y)

myfun()
print(x)