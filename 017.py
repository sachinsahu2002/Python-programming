l = [2,4,6,8,9,11,44,67,98,24,5]
# print(l)
# l.append(7)
# l.sort(reverse=True) #Sorting and reversing is done
# l.reverse() #directlty reverse without sorting
# l.insert(0,3)
print(l.index(98))
print(l.count(9))
# finding something in list
if 44 in l:
    print(l.index(44))

# copy of list
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)
l.extend(colors) #extends l by adding colors to it
print(l)

k = l+newlist
print(k)
