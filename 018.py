#Tuple in python
tup =(1,3,4,6,7,9,0,"Round",True)
print(type(tup))
# tup[0] = 9 #throws error since tuple are immutable
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])

tup2 = tup[1:4]
print(tup2)
if 9 in tup:
    print(tup.index(9))
