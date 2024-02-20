# F-string in python 

letter = "Hi, This is {1}. And I'm {0} years"
name = "Sameer"
country = "India"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")

print(f"We use F-string like this: Hey my name is {{name}} and I am from {{country}}")

price = 49.09999
print(f"For only {price:.2f} dollars!")