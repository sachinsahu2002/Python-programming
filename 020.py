# Create a program capable of displaying questions to the user of KBC.
# Use list data type to store the questions and their correct answer.
# Display the final amount the user is taking home after playing the game.
a = [
     "The term “app”, in the context of a mobile app, is a shortened form of which word?\n(A)Apple\n(B)Apparel\n(C)Apparatus\n(D)Application",
     "According to our Union Ministry of Health and WHO, you should wash your hands with soap and water for at least how many seconds to prevent the spread of COVID-19?\n(A)1 – 5 seconds\n(B)5 – 10 seconds\n(C)10 – 15 seconds\n(D)20 – 30 seconds\n",
     "Which river passes through marble stones in Bhedaghat in Madhya Pradesh?\n(A)Chambal\n(B)Narmada\n(C)Shipra\n(D)Betwa",
     "Who is the current Prime Minister of Canada?\n(A)Boris Johnson\n(B)Angela Merkel\n(C)Justin Trudeau\n(D)Justin Trudeau",
     "In January 2020, Rani Rampal became the first-ever player in which sport to win the ‘World Games Athlete of the Year 2019’ award?\n(A)Hockey\n(B)Table Tennis\n(C)Cricket\n(D)Football",
     "A professional examination board popularly called Vyapam conducts various tests for admission to professional courses in which of these states?\n(A)Gujarat\n(B)Uttar Pradesh\n(C)Rajasthan\n(D)Chhattisgarh",
     "According to Mahabharata, who among these was not Arjuna’s wife?\n(A)Subhadra\n(B)Ulupi\n(C)Devika\n(D)Chitrangada",
     "The release of which chemical led to the Bhopal gas tragedy in 1984?\n(A)Hydrogen azide\n(B)Methyl isocyanate\n(C)Dicholorosilane\n(D)Silicon Tetrachloride",
     "Written by former Lok Sabha Speaker Sumitra Mahajan, the book ‘Matoshree’ is based on which Indian queen?\n(A)Rani Lakshmibai\n(B)Rani Padmini\n(C)Rani Durgavati\n(D)Rani Ahilyabai Holkar",
     "Who actually invented the telescope in 1608?\n(A)Johannes Kepler\n(B)Nicolaus Copernicus\n(C)Hans Lippershey\n(D)Galileo Galilei",
     "In 2008, Rajasthan Royals became the first winner of which annual sporting event?\n(A)PKL\n(B)ISL\n(C)PHL\n(D)IPL",
     "What are the terms 3G, 4G, and 5G related to?\n(A)Population Generations\n(B)Phone Networks\n(C)Digital Camera\n(D)Grading in Schools",
     "Which of the following will be heavier than 1450 gm of iron?\n(A)1 Kg of Rice\n(B)1.4 Kg of Paper\n(C)1.7 Kg of Cotton\n(D)1.3 Kg of Husk",
     "Which of these songs about rain does not have any rain sequence?\n(A)Tip Tip Barsa Paani (Mohra)\n(B)Rimjhim Gire Saawan (Manzil)\n(C)Barso Re (Guru)\n(D)Ghanan Ghanan (Lagaan)",
     "Which of the following states doesn’t share its boundary with Gujarat?\n(A)Maharashtra\n(B)Rajasthan\n(C)Madhya Pradesh\n(D)Goa",
     "According to Indian Mythology, Kans, the brother of Devaki was the ruler of which city?\n(A)Mathura\n(B)Dwarka\n(C)Indraprastha\n(D)Ujjain",
     "Who wrote the play “Romeo and Juliet”?\n(A)Oscar Wilde\n(B)William Shakespeare\n(C)Jane Austen\n(D)F. Scott Fitzgerald",
     ]

b = ["d","d","b","c","a","d","c","b","d","c","d","b","c","d","d","a","b"]

# c = ["1,000","2,000","5,000","10,000","20,000","50,000","1,00,000","2,00,000","5,00,000","10,00,000","20,00,000","50,00,000","1,00,00,000","2,00,00,000","3,50,00,000","5,00,00,000","7,00,00,000","0"]
c = ["0","1,000","2,000","5,000","10,000","20,000","50,000","1,00,000","2,00,000","5,00,000","10,00,000","20,00,000","50,00,000","1,00,00,000","2,00,00,000","3,50,00,000","5,00,00,000","7,00,00,000"]

# def sol(ans,x):
#     # try:
#     if ans == b[x]:
#         print("Correct answer")
#         print(c[x])
#     else:
#         print("Wrong")
#         print(c[x-1])
#     # finally:print(c[x])

     
# Use 1st c list to get correct output
# for items in a:
#     print(items)
#     x = a.index(items)
#     ans = input("\nEnter your Answer option: ")
#     # print(ans,x)
#     # sol(ans,x)
#     if ans == b[x]:
#         print("\nCorrect answer")
#         print("\nYou won Rs ",c[x],"\n")
#     else:
#         print("\nWrong answer")
#         print("\nYou won Rs ",c[x-1]," in KBC\n\n")
#         break

# Use 2nd c list to get correct output
import random
for i in range(1,18):
    s = random.choice(a)
    print("Q. no.",i,"For Rs",c[i])
    print(s)
    x = a.index(s)
    ans = input("\nEnter your Answer option: ")
    if ans == b[x]:
        print("\nCorrect answer")
        print("\nYou won Rs ",c[i],"\n")
    else:
        print("\nWrong answer")
        print("\nYou won Rs ",c[i-1]," in KBC\n\n")
        break
    a.pop(x)
    b.pop(x)