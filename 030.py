#Else statement withe for and while loop in python

# for i in range(5):
#     print(i)
#     if i == 4:
#         break
# else:
#     print('Sorry no i;')

# i = 0
# while (i < 7):
#     print(i)
#     i = i+1
#     if i == 4:
#         break
# else:
#     print('Sorry no i;')

for x in range(5):
    print("For iteration no {} this is loop".format(x+1))
else:
    print("Else part in loop")
print("Out of Loop")