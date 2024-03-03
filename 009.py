# Match case statement
# Match case statements are used to match the case statements if mathch found then that statement is executed
a = int(input("Enter a number: "))
# a is variable to match
match a:
    # if a is 0
    case 0:
        print("a is zero")
    case 4:
        print("Case is 4")
    # default cases are represented by _
    case _ if a!=90:
        print(a, " is not 90")
    case _ if a!=80:
        print(a, " is not 80")
    case _:
        print(a)
    
