# def average(a=6,b=2):
#     print("The average is:", (a+b)/2)

# # average(4,6)
# average(b=4)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is: ", sum)
    # return 7
    return sum/len(numbers)

c = average(5,2,8,3,9)
print(c)

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

