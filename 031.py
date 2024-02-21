# Exception Handling in python
a = input("Enter your number:")
print("Multiplication table of ",a)
try:
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")
except:
    print("Invalid Input!")

print("Some imp lines of code")
print("End of program")

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")

