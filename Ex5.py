# Exercise 5 Game of Snake, Water, Gun a variant of Rock, Paper, Scissor 
# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" 
# where players use hand gestures to represent a snake, water, or a gun. 
# The gun beats the snake, the water beats the gun, and the snake beats the water. 
# Write a python program to create a Snake Water Gun game in Python using if-else statements. 
# Do not create any fancy GUI. Use proper functions to check for win.

#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

# Logic
# def res(y,z):
#     if (y>z):
#         return("Won")
#     elif (y<z):
#         return("Lose") 
#     else:
#        return("Draw")

# import random
# opt = ["Snake","Water","Gun"]
# print("RULE: Select 0 for Snake, 1 for Water or 2 for Gun\n")
# n = int(input("Enter number of matches of Tournament you want to play: "))
# a = 0
# b = 0
# for i in range(n):
#     z = random.choice(opt)
#     com = opt.index(z)
#     reply = int(input("\nSnake, Water or Gun: "))
#     print(f"\nComputer: {z}, You: {opt[reply]}\n")
#     if reply==0 and com==1:
#         print("You Win")
#         a += 1
#     elif reply==0 and com==2:
#         print("You Lose")
#         b += 1
#     elif reply==1 and com==0:
#         print("You Lose") 
#         b += 1
#     elif reply==1 and com==2:
#         print("You Win")
#         a += 1
#     elif reply==2 and com==0:
#         print("You Win")
#         a += 1
#     elif reply==2 and com==1:
#         print("You Lose")
#         b += 1
#     else:
#         print("Match Draw")
# print(f"\nYou Won {a} matches and Compuer won {b} matches in the Tournament")
# print(f"\nYou {res(a,b)} the tournament")

def res(y,z):
    if (y>z):
        return("Won")
    elif (y<z):
        return("Lose") 
    else:
       return("Draw")

import random
opt = ["Rock","Paper","Scissor"]
print("RULE: Select 0 for Rock, 1 for Paper or 2 for Scissor\n")
n = int(input("Enter number of matches of Tournament you want to play: "))
a = 0
b = 0
for i in range(n):
    z = random.choice(opt)
    com = opt.index(z)
    reply = int(input("\nRock, Paper or Scissor [enter 0,1 or 2]: "))
    print(f"\nComputer: {z}, You: {opt[reply]}\n")
    if reply==0 and com==1:
        print("You Lose")
        b += 1
    elif reply==0 and com==2:
        print("You Win")
        a += 1
    elif reply==1 and com==0:
        print("You Win")
        a += 1
    elif reply==1 and com==2:
        print("You Lose") 
        b += 1
    elif reply==2 and com==0:
        print("You Lose")
        b += 1
    elif reply==2 and com==1:
        print("You Win")
        a += 1
    else:
        print("Match Draw")
print(f"\nTotal you Won {a} and Computer won {b} matches in the Tournament")
print(f"\nYou {res(a,b)} the Tournament\n")