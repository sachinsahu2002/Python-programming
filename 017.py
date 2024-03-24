l = [2,4,6,8,9,11,44,67,98,24,5]
# print(l)
# l.append(7)
# l.sort(reverse=True) #Sorting and reversing is done
# l.reverse() #directlty reverse without sorting
# l.insert(0,3)
# print(l.index(98))
# print(l.count(9))
# # finding something in list
# if 44 in l:
#     print(l.index(44))

# # copy of list
# colors = ["voilet", "green", "indigo", "blue"]
# newlist = colors.copy()
# print(colors)
# print(newlist)
# l.extend(colors) #extends l by adding colors to it
# print(l)

# k = l+newlist
# print(k)

nums = [1,0,0,-1,2,3,0,0,0,0,1,2,2,3,4,5,5,6,7,8,9,8,7,9,8,7]
for item in nums:
    a = item
    b = nums.count(a)
    if (b>2):
        while b>2:
            nums.remove(a)
            b = nums.count(a)
nums.sort()
print(nums)

# nums1 = [item for item in nums1 if item!=0]
# print(nums1)
# if (len(nums2)==0):
#     print(nums1)
# else:
#     nums1 = nums1 + nums2
#     nums1.sort()
#     print(nums1)