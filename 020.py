# Create a program capable of displaying questions to the user of KBC.
# Use list data type to store the questions and their correct answer.
# Display the final amount the user is taking home after playing the game.
a = ["How are you?\n(a)Fine\n(b)Good\n(c)Very good\n(d)Excellent",
     "Besides Sachin Tendulkar, who is the only other Indian cricketer to have scored over 13,000 runs in test cricket?\n(a)Virat Kohli\n(b)Sunil Gavaskar\n(c)VVS laxman\n(d)Rahul David",
     "Ranthambore, Sariska and Keoladeo Ghana are all names of what?\n(a)National Parks\n(b)Goosebumps\n(c)Mountains\n(d)Rivers"]

b = {"How are you?\n(a)Fine\n(b)Good\n(c)Very good\n(d)Excellent":"a",
     "Besides Sachin Tendulkar, who is the only other Indian cricketer to have scored over 13,000 runs in test cricket?\n(a)Virat Kohli\n(b)Sunil Gavaskar\n(c)VVS laxman\n(d)Rahul David":"d",
     "Ranthambore, Sariska and Keoladeo Ghana are all names of what?\n(a)National Parks\n(b)Goosebumps\n(c)Mountains\n(d)Rivers":"b"}

def sol(ans):
    for values in b:
        if ans == b.get("How are you?\n(a)Fine\n(b)Good\n(c)Very good\n(d)Excellent"):
            print("correct")
        else:
            print("Wrong")
            break

     

for items in a:
    print(items)
    ans = input("Enter your Answer option: ")
    sol(ans)