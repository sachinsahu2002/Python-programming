# Methods of dictionary in python
a = {234:55,456:70,232:65,654:40,222:80}
b = {939:70,341:65,431:72}

#update()
a.update(b)
print(a)

#clear()
b.clear()
print(b)

#pop() One at a time
a.pop(456)
print(a)

# popitem()
a.popitem()
print(a)

# del used to delete the dictionary 
del b
print(a)

