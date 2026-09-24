# TUPLES : works with immutable sequences
# they are like lists only , but they can not be changed once created

# Empty tuple 
tup = ()

# for single tuple comma is mandatory
single = (42 , )

not_tuple = (42)
# above is wrong

# tuple with multiple items 
cords = (4 , 5)
colors = ('red' , 'green' , "blue" , "orange")

# accessing element of tuple
colors[0]

# lets try to update it
colors[2] = 'purple'
# it gave error bcs tuples are immutable

colors[0 : 3]
# red green blue orange

