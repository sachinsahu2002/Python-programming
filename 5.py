#string methods
a = "!!!!The magician made a magical mat!!! @@@"
#convert in uppercase
print(a.upper())
# Convert in lower case
print(a.lower())
#removing symbols after the sentence
print(a.rstrip("@"))
# Replacing the string
print(a.replace("magic", "logic")) #this is case sensitive if you write Magic instead of magic it doesn't works
# Making list from String
print(a.split("a"))

blog = "introduction to python programming"
print(blog.capitalize()) #Capitalizes only first letter

str1 = "Welcome to the console!!!!"
print(len(str1))
print(str1.center(50)) #total len keeps 50 ie add 24, 12 in front and back
print(len(str1.center(50)))

# counting occurances of a string
print(a.count("!"))
#checking the ends with some string
print(str1.endswith("!"))






