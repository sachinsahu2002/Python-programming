# For loop in python
name = "Rohan"
for i in name:
    print(i)
    if (i=="h"):
        print("this is special")

colors = ["Red","Blue","Green","Yellow"]
for color in colors:
    print(color)
    for j in color:
        print(j)

for k in range(5):
    print(k+1)

for k in range(1,202):
    print(k, end=" ")

for k in range(1,12,3):
    print(k)