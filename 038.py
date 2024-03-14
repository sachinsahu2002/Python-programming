#Enumerate function
# Helps to loop over a sequence (such as list, tuple or string) and get the index value of each also
# It is capable to begin the index as per our choice

Animals = ["Lion","Tiger","Liger","Cat","Dog"]
for index, Animal in enumerate(Animals):
    print(index, Animal)

a = "Sachin"
for i,a in enumerate(a,4):
    print(i,a)