# Dictonaries : Stores data with key - value pairs
# think of it like a real dict where you look up for a word(key)
# to find its meaning (value)

# real - world ex:
#  name > phn no.
# dish > price

person = {
    "name" : "kirti",
    "age" : 25,
    "city" : "majra"
}

# accessing the dict
person

# accessing particular ele of dict
person["age"]

# we can also chnge the value
person["name"] = "rana ji"
person

# we can add new par in dict
person["legal"] = True
person

# we can also delete
del person["age"]
person

# DICTIONARY METHODS
print(person.keys())
print(person.values())
print(person.items())


if "name" in person:
    print("name found")

# if m yhn pr name ki jgah rana ji , koi bhi value likhu then it will not work bcs we can write key only not its value

# UPDATE multiple values
person.update({"city":"rajgarh" , "part":True})
person

# yhn pr dict me hmare pas part key avail ni tha but ab update krne k bad part b add on hoga dic me







