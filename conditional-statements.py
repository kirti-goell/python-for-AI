# if , elif , else
#  the first true condition wins
# we can not have elif without if and also we can not have else without if
# we can have if without else or elif and without both

# if
age = 20
if(age>=25):
    print("eligible")
#  will not print anything

age = 20
if(age >= 18):
    print("eligible")
# will print eligible


# if - else
is_student = True
if(is_student == True):
    print("you are a student")
else:
    print("you are not a student")



# if - elif - else
marks = 80
if(marks >= 80):
    print("A")
elif(marks >= 70):
    print("B")
elif(marks >= 60):
    print("C")
else:
    print("you need to improve")

#  here ques arises 80 >= 80 and 80 >= 70 and 80 >= 60 then why it is printing op as A 
# bcs the first true condition wins : its the golden rule of python



# if vs elif
x = 80
if(x >= 80):
    print("A")
if(x >= 70):
    print("B")
# A B both we will get the op bcs of multiple if thats why elif is needed

x = 80
if(x >= 80):
    print("A")
elif(x >= 70):
    print("B")
# A is the op



# Conditions with and / or / not
age = 20
has_id=True
if(age >=20 and has_id):
    print("eligible to go inside")



day = "saturday"
if(day == "saturday" or day == "sunday"):
    print("its weekend")


is_student = True
if(not is_student):
    print("True")
else:
    print("False")




# Membership conditions
fruit = "papaya"
if(fruit in ["apple", "mango", "banana"]):
    print("fruit found")
else:
    print("fruit not found")


name = "tanyaA"
if("A" in name):
    print("found")
else:
    print("not found")


name = "tanyaA"
if("A" not in name):
    print("not found")
else:
    print("found")



# Python has truthy and falsy values

is_logged_in = True
# so we can write it as 
# if (is_logged_in):


is_avail = False;
if(is_avail):
    print("available")
else:
    print("not available")

# means if avail == true, return  available else not available

# python considers some values as falsy such as 
# None
# False
# 0
# 0.0
# ""
# []
# {}
# set()

name = "Shree"
if(name):
    print("name exists")
else:
    print("name does not exist")
# bcs of non empty string exist in name


# None case
res = None
if(res is None):
    print("no such result")
else:
    print("result exists")

# for None remember this pattern
# if(res is not None) := is not case 