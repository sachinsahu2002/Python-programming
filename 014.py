# functions in Python
def geometricMean(a,b):
    geometricMean = (a*b)/(a+b)
    print(geometricMean)

def isGreater(a,b):
    if (a>b):
        print("First number is greater than second")
    else:
        print("Second number is greater or equal")

def isLesser(a,b):
    pass

a = 5
b = 6
geometricMean(a,b)
# geometricMean1 = (a*b)/(a+b)
# print(geometricMean1)
isGreater(a,b)

c = 7
d = 2
geometricMean(c,d)
# geometricMean2 = (c*d)/(c+d)
# print(geometricMean2)
isGreater(c,d)