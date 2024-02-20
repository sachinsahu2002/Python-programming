# Methods of Stws in py

a = {"Carla", "Jack","Tango",5,8.6,"Aman",2}
b = {"Country","World","State","District","Tango"}

#Union of sets and Updation
c = a.union(b)
print(c)
a.update(b) #if you print this you get None
print(a) # Here a is updated
print(b)

#Intersection and intersection_update of set
a = {"Carla", "Jack","Tango",5,8.6,"Aman",2}
b = {"Country","World","State","District","Tango"}
d = a.intersection(b)
print(d)
b.intersection_update(a)
print(b)

#Symmetric difference and symmetric difference update 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

#Difference and Difference update 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.difference_update(cities2)
print(cities)
