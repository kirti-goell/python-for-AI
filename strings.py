# String : Text written inside single / double quotes
# city = "Shimla"
# course = "AI Engineering"
# message = "I want to become an AI Engineer"
# phone = "9876543210"

# string is a sequence

# Strings can contain spaces , therefore space is also a part of a string

# we can access the string / particular character of a string
name = "kirti"
print(name)
print(name[0])

# python also allows us for negative indexing
# K   i   r   t   i
# 0   1   2   3   4
# -5 -4  -3  -2  -1

print(name[-2])
# t

print(type(name))
type(name)

# what happens if index does not exist
print(name[5])
# IndexError

# length of string
len(name)
# 5

name = "Kirti Goel"
print(len(name))
# 10
print(name[5])
# space

# K i r t i _ G o e l
# 1 2 3 4 5 6 7 8 9 10
# space is also counted


# slicing : taking a part of a string
# string[start : end]

name[3 : 9]
# ti Goe

# can also leave out the beginning or end or both
name[:7]
# from start to the 6th idx
name[3:]
# from 3rd idx to the whole str
name[:]
# return full string



# slicing with step
# string[start : end : step]
# K i r t i _ G o e l
# 0 1 2 3 4 5 6 7 8 9
name[3 : 10 : 2]


# reverse string
name[::-1]


# strings are immutable
name = "abcdef"
name[3] = "z"
# this will give error
# I cannot modify the existing string character-by-character; I need to create a new string.



#  joining strings
first_name = "Kirti"
last_name = "Goel"
full_name = first_name + " " + last_name
print(full_name)


# Repeating strings
print("Hi "*3)
print("*" * 5)


# in-built methods of string
name = "kirti"

# 1. to upper case
print(name.upper())

# 2. to lower case
print(name.lower())

# 3. to capitalize the first letter
print(name.capitalize())
# Kirti

# 4. to remove extra spaces from start and end only
name = "   Kirti   "
print(name.strip())


# replace text
text = "I love Java"
text = text.replace("Java", "Python")
print(text)


# searching inside text
text = "I am learning Python"
print("Python" in text)
# True

# find() returns the starting index of letter
text = "I am learning Python"
print(text.find("Python"))
# 14

print(text.find("Java"))
# -1 bcs java does not exist


# counting something
text = "banana"
print(text.count("a"))
# 3


# split() : converts a string of words into list of words
sentence = "I love Python"
words = sentence.split()
print(words)
# ['I', 'love', 'Python']


# join() : opposite of split() , list of words -> string of words
words = ['I', 'love', 'Python']
sentence = " ".join(words)
print(sentence)


# f-strings : formatted string means putting variable inside string
name = "kirti"
age = 22
print(f"My name is {name} and I am {age} years old.")
print(name.startswith("I"))
# False
print(name.endswith("i"))
# true
print(name.endswith("I"))
# false

str = "heLLO WORLD"
str = str.title()
print(str)
# Hello World




# 🧠 Your String Cheat Sheet
# Concept	                            Example
# Create string	                      name = "Kirti"
# Type	                              type(name)
# Length	                          len(name)
# Character                           name[0]
# Last character	                  name[-1]
# Slice	                              name[0:5]
# Reverse	                          name[::-1]
# Uppercase	                          name.upper()
# Lowercase	                          name.lower()
# Remove spaces	                      name.strip()
# Replace	                          name.replace("a", "b")
# Search	                          "Python" in text
# Find position	                      text.find("Python")
# Count	                              text.count("a")
# Split	                              text.split()
# Join	                              " ".join(words)
# Combine	                         first + last
# Insert variables	                 f"Hello {name}"