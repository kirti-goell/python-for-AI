# what is a variable? :=  variable is a name that refers to some value/data
# age = 22 where age is variable , = is assignment operator , 22 = value

# --------------------------------------------------------------------------

# Creating a variable := python does not require to declare the type first like int , bool , etc.
# python automatically understands the type 

# ---------------------------------------------------------------------------

# Variables can hold diff types
# 1. Integer => int
# age = 22
# temp = -5

# 2. Decimal => float
#  price = 99.9

# 3. String => str
# name = "kirti"

# 4. Boolean => bool
# is_stu = True
# is_allowed = False

# 5. None => None (no value / absence of value)
# res = None

# -----------------------------------------------------------------------

# How to check the type of variable? :  type()
student = 5
print(type(student))
# <class 'int'>
type(student)
# int

# ------------------------------------------------------------------

# Python is dynamically typed language
x = 10
type(x)
# int

x="kirti"
type(x)
# str

# --------------------------------------------------------------------------

# Rules for naming vriables
# Rule1 : letters , numbers , _ are allowed like age, is_person , people2
# Rule2 : var cannot start with number like 2name
# Rule3 : no spaces like my self
# Rule4 : python is case-sensitive like age , Age , AGE are different vars

# ---------------------------------------------------------------------------

# Reserved keywords : can not use them as variable name
# if , else , for , while , class , def , return , True , False , None

# ------------------------------------------------------------------------------

# Assigning multiple vars
# name, age, sector = "kirti", 20, 12
# it is equivalent to : name = kirti , age = 20, sector = 12

# a=b=c= 10

# ---------------------------------------------------------------------------

# Changing variables value
y = 10
print(y)
# 10

y = 20
print(y)
# 20

# ------------------------------------------------------------------------------

# Variables with strings
first_name = "kirti"
last_name = "goel"

full_name = first_name + " " + last_name
print(full_name)

# " " is a string of space

# -------------------------------------------------------------------------

# Variable + string using f-string means formatted string
name = "kirti"
age = 22
print(f"My name is {name} and i am {age} years old")

# without writing f it will be like {name} only
# with f {name} is getting replaced by actual value i.e. kirti

one = 1
two = 2
print(f"{one}{two}")
# 12

one = 1
two = 2
print(f"{one} {two}")
# 1 2

#  ------------------------------------------------------------------------------------

#  Diff between = and ==
# = means assignment operator 
# == means comparison operator

age = 22
print(age==22)
# True

# ----------------------------------------------------------------------------------------

# Taking input and storing it into a variable
# by def its type is str even if you give float , bool , int
name = input("Enter your name : ")
print(name)

age = input("Enter your age : ")
print(age)
print(type(age))

# -----------------------------------------------------------------------------------------------

# Converting input to int , float
age = int(input("Enter your age : "))
print(age)
print(type(age))

age = float(input("Enter your age : "))
print(age)
print(type(age))

# -------------------------------------------------------------------------------------------------------------------------------

# Variable type conversion
# 1. str -> int

x = "10"
x = int(x)
print(x)
type(x)

# 2. int -> str
x = 10
x = str(x)
print(x)
type(x)

# int -> float
x = 20
x = float(x)
print(x)
type(x)

# float -> int
x = 33.3
x = int(x)
print(x)
type(x)

# str -> int 
x = "hello"
x = int(x)
print(x)
# this will give an error

# -------------------------------------------------------------

age = "20"
# print(age + 5)
#  this will give an error bcs of str + int

print(int(age) + 5)
# 25

# ----------------------------------------------------------------------

# a variable can refer to many different kind of python objects

# there are most important python data structures
# 1. LIST : like a shopping list (ordered items)
# numbers = [1,3,5]
# 2. DICTIONARY : like a phone book (name > number) 
# {"name": "rahul", "age": 22}
# 3. SET : like a bag of unique items
# unique_numbers = {1, 2, 3}
# 4.TUPLE : like coordinates (fixed values)
# coordinates = (10,20)

# ----------------------------------------------------------------------------

# Take users age as input and print : you are 22 years old
age = int(input("Enter age: "))
print(f"you are {age} years old.")
















