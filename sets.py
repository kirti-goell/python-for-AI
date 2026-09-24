# SETS : works with unique collection
# they automatically removes duplicate

# ex : guest list (each person once)

# empty set
emp_set = set()
# not {}, bcs thats dict

# set with values : both wYays works
number = {1 , 2 , 3 , 4}
fruits = set(['apple' , 'banana'])

vals = [1 , 1 , 5 , 8 , 10 , 12]
unique_val = set(vals)
unique_val
# 1 5 8 10 12

sets = set(["a" , "b", "c","a" , "b", "c"])
sets
# a b c

# basic operations 

sets.add("KLMNOP")
sets
# this above value will be get added 

sets.remove("a")
# .remove gives error if that value not found


sets.discard("k")
# .discard does not gives error even if that value not found
sets

