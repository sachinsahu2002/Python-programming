# Manipulating tupple
countries = ("Spain","Russia","China","Japan")
temp = list(countries)
temp.append("Finland")
temp.pop(2)
temp[0] = "India"
countries = tuple(temp)
print(countries)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = tuple1.count(3)
# res = tuple1.index(3) #Gives first occurance of 3
# res = tuple1.index(3, 4, 8)  #Gives first occurance of 3 between 4:8
res = len(tuple1)
print('Count of 3 in Tuple1 is:', res)