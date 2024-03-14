# string slicing
name = "Param,Raman"
print(len(name))
print(name[0:5])
fruit = "Pineapple"
frlen = len(fruit)
print(frlen)
print(fruit[0:9])
print(fruit[2:])
print(fruit[2:6])
print(fruit[2:-3]) # print(fruit[2:len(fruit)-3]) i.e. [2:9-3] = [2:6]
print(fruit[-2:-3]) # print(fruit[len(fruit)-2:len(fruit)-3]) = [9-2:9-3] = [7:6] thus not get printed
print(fruit[-4:-3]) # print(fruit[len(fruit)-4:len(fruit)-3]) = [9-4:9-3] = [5:6]

# reversing a string
a = "Jack"
print(a[::-1])

