# Raising Custom Errors
# a = int(input("Enter number in multiple of 5: "))
# if not (a%5==0):
#     raise ValueError("Value is not in multiple of 5")

a = input("Enter any value between 5 and 9 or quit:")
b = type(a)
# print(b)
if b == str and a == "quit":
  print("quit")
elif(int(a)<5  or int(a)>9):
  raise  ValueError("Value should be between 5 and 9 or quit")
