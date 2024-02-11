# Break and Continue satements
for i in range(14):
    if(i==10):
        break
    print("5 X", i+1, "=",5*(i+1))
print("Leaves the loop")
#Value of i do not increase if you once use break 
for i in range(12):
    if(i==10):
        print("Skip the iteration")
        continue
    print("5 X", i+1, "=",5*(i+1))
#Value of i increases if you use continue till the end of loop