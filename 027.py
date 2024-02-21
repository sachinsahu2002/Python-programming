#Dictionary in python

info = {"name":"Karan", "Age":25, "eligible": "True"}
print(info)
# Accessing Single elements
print(info["name"])
print(info.get("fit"))

# Accessing Multiple elements
print(info.keys())
print(info.values())
print(info.items())

# for key in info.keys():
#     print(f"The values corressponding to key {key} is {info[key]}")

for key, values in info.items():
    print(f"The values corresponding to key {key} is {values}")


