# Methods of Set in py continued
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))
print(cities.issuperset(cities2))
print(cities2.issubset(cities))

#Adding, removing/discarding elements of a set
# Can add or remove only one item at a time
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("kyo")
print(cities)

# Pop, del, clear
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)
del cities
# print(cities)

print(type(item))
cities2.clear()
print(cities2)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")