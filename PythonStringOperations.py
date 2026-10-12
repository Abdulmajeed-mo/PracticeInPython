# Python String Operations
# = name of this not equal , its Assignment operator

my_language = "Python is a programming language"
framework = "Django is a web framework"



# Accessing characters in a string in start
print(my_language[0])  # Output: P

# Accessing characters in a string in end
print(my_language[-1])  # Output: n

# Slicing strings
print(my_language[0:3])  # Output: Pyt

# Concatenation of strings
full_string = my_language + " " + framework
print(full_string)  # Output: Python Django


#formatting strings
print("I love {} and {}".format(my_language, framework))  

# upper
print(my_language.upper())  
# lower
print(my_language.lower())

# strip

print(full_string.strip()) 

#count
print(my_language.count("a"))  