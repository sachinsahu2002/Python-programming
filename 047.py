# MAP, FILTER, REDUCE 
# MAP
a = [2,3,4,7,8,9,5]
sqra = map(lambda x:x*x, a)#(function, iterable)
print(list(sqra))

# FILTER
b = [2,4,7,9,10,24,57,98,34]
evn = filter(lambda x: x%2, b)
print(list(evn))
c = "Jackismyfriend"
sp = filter(lambda char: char=="a" or char=="e" or char=="i" or char=="o" or char=="u", c)
print("".join(list(sp)))

# REDUCE
from functools import reduce
b = [2,4,7,9,10,24,57,98,34]
sum = reduce(lambda x,y: x+y, b)
print(sum) # NO need to typecast the answer obtained from reduce