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

str1 = "Welcome to the console!!!! of HTML5"
print(len(str1))
print(str1.center(50)) #total len keeps 50 ie add 24, 12 in front and back
print(len(str1.center(50)))

# counting occurances of a string
print(a.count("!"))
#checking the ends with some string
print(str1.endswith("!"))
#checking the range of string ending with some string
print(str1[2:10].endswith("too"))

#find string inside string
print(str1.find("th"))
 
# checkng for alphanumeric in strings
print(str1.isalnum())
print(str1.isalpha())
print(str1.islower())
print(str1.isprintable())
print(str1.isspace())
print(str1.istitle())
print(str1.swapcase())
print(str1.startswith("Welcome")) #checking for staring of the string
print(str1.title()) #convert the string to python













