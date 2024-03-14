# file = "File1"
# loc = "C:\Users\admin\OneDrive\Documents\HTML"
# path = join(loc,file)

# f = open("..\HTML\File1.txt", 'b')
# text = f.read()
# print(text)
# f.close()

# In above you need to manually close the opened file
# With statement: this allows no need for file closing
with  open("File1.txt", 'a') as f:
    f.write("\nThis line is being appended in this file")
with  open("File1.txt", 'r') as f:
    text = f.read()
    print(text)
