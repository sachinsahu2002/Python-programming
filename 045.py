#seek(), tell(), truncate()

# f = open('File1.txt', 'r')
# f.seek(10)
# data = f.read(10)
# print(data)
# f.close()

# f = open('File1.txt', 'r')
# data = f.read(10)
# a = f.tell()
# print(data)
# print(a)
# f.close()

f = open('File1.txt', 'w')
data = f.write("Hi this is Jack")
f.truncate(5)
f.close()