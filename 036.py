# Exercise 4: Secret Code Language
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

# x = input("Enter word: ")
# if len(x)>3:
#     x = "abc"+x[1:]+x[0]+"xyz"
# else:
#     x = x[::-1]
# print(x)

# x = input("Enter word: ")
# if len(x)>3:
#     x = x[-4]+x[3:-4]
# else:
#     x = x[::-1]
# print(x)

import random
import string
# r = ''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase, k=6))
# s = str(r)

# a = int(input("Press 1 for coding or 0 for decoding: "))
# mes = input("Enter your message: ").split(" ")
# z = ""
# l = len(mes)
# if a == 1:
#     for i in range(l):
#         b = mes[i]
#         # print(b, len(b))
#         if len(b)<3:
#             b = b[::-1]
#             # mes[i] = b
#             z += b+" "
#         elif len(b)>=3:
#             r = ''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase, k=6))
#             s = str(r)
#             b = s[:3] + b[1:] + b[0] + s[3:]
#             # print(b)
#             # mes[i] = b
#             z += b+" "  
#     print(z)
# if a == 0:
#     for i in range(l):  
#         b = mes[i]
#         if len(b)>=3:
#             b = b[-4]+b[3:-4]
#             # mes[i] = b
#             z += b+" "
#         else:
#             b = b[::-1]
#             # mes[i] = b
#             z += b+" "
#     print(z)

a = int(input("Press 1 for coding or 0 for decoding: "))
mes = input("Enter your message: ").split(" ")
z = []
l = len(mes)
if a == 1:
    for i in range(l):
        b = mes[i]
        # print(b, len(b))
        if len(b)<3:
            b = b[::-1]
            # mes[i] = b
            z.append(b)
        elif len(b)>=3:
            r = ''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase, k=6))
            s = str(r)
            b = s[:3] + b[1:] + b[0] + s[3:]
            # print(b)
            # mes[i] = b
            z.append(b) 
    print(" ".join(z))
if a == 0:
    for i in range(l):  
        b = mes[i]
        if len(b)>=3:
            b = b[-4]+b[3:-4]
            # mes[i] = b
            z.append(b)
        else:
            b = b[::-1]
            # mes[i] = b
            z.append(b)
    print(" ".join(z))
    

