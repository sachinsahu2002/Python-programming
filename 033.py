# head = [1,2,3,4,5]
# a = len(head)
# # print(a)
# # print(type(a))
# # print(head[int((a-1)/2):])
# # if (a%2 == 0):
# #     print(head[int(a/2):])
# # else:
# #     print(head[int((a-1)/2):])

# print(head.get(int(a/2)))
ransomNote = "aacdrfh"
magazine = "aabcdefghtresjukilgg"
# while (len(ransomNote) != 0):
for chars in ransomNote:
    b = chars
    if b in magazine:
        ransomNote.remove("b")
        magazine.remove("b")
    else:
        print(False)
        break
else:
    print(True)
#     r.append(b)
# print(r)
# print(m)
# for items in r:
#     x = items
#     if x in m:
#         r.remove(x)
#         m.remove(x)
#         if r == []:
#             print(True)
#     else:
#         print(False)

# if (r in (m)):
#     print(True)
# else:
#     print(False)

    # if a in ransomNote:
    #     ransomNote.replace(a,'')
    #     magazine.replace(a,'')
    #     print(ransomNote)
    #     print(magazine)
    #     # else:
    #     #     print(False)