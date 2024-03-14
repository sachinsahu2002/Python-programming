# read(), readline(), readlines(), write(), writelines() methods

# f = open('File1.txt', 'r')
# i = 0
# while True:
#     i += 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(',')[0]
#     m2 = line.split(',')[1]
#     m3 = line.split(',')[2]
#     print(f"This is marks of student {i} in Maths: {m1}")
#     print(f"This is marks of student {i} in English: {m2}")
#     print(f"This is marks of student {i} in GK: {m3}")

# f = open('File1.txt','r')
# line = ["Line1\n","Line2\n","Line3\n","Line4\n"]
# a = f.readlines() # Reads single line readlines() Reads all lines till termination of lines in file
# print(a)
# f.close

# f = open('File1.txt','r')
# line = ["Line1\n","Line2\n","Line3\n","Line4\n"]
# f.writelines() # Write lines in a file
# f.close

f = open('File1.txt','w')
lines = ["Line1\n","Line2\n","Line3\n","Line4\n"]
for line in lines:
    f.write(line + '\n')
f.close