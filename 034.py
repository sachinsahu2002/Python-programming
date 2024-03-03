# Finally Clause in python
# New thing to be noted when you print a function then only th return statements are executed 
# Only if call a function then return statements are not executed instead print statements are executed if present
def funct1():
    l = ["a","b","c","d","e","f"]
    n = int(input("Enter the index: "))
    try:
        # print(l[n])
        return("Yes")
    except:
        # print("Some Error occurred")
        return("Dance")
    finally:
        print("I am always executed")

x = funct1()
print(x)