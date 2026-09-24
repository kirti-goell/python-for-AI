# LISTS : lists are pythons most versatile data structure. 
# They were like containers which can hold multiple values in specific order

has_license = True
age = 23
my_list = ["allice" , age , 10 , has_license , False , "Bob"]

# accessing elements from list
my_list[0]
# allice
my_list[5]
# bob
my_list[-1]
# bob
my_list[-3]
# true

my_list

# updating the element of list
my_list[0] = "dave"
my_list[0]
# dave

my_list


# we can add other elemts to the list at the end
my_list.append("paonta sahib")
my_list
# paonta sahib will be appended to the end of the list

# we can add ele at particular index
my_list.insert(3,"money")
my_list

# we can remove ele from list
my_list.remove(23)
my_list

# we can remove the last ele of list
last = my_list.pop()
last
my_list


len(my_list)
# 6
print(my_list.count('money'))
# 1
my_list.index(False)
# 4


numbers = [7 , 4 , 3, 0, 9 , 9, 18, 4 , 1 , 0]
# sorting list
numbers.sort()
# now numbers list got sortd

# reverse list
numbers.reverse()
print(numbers)
# yhn pr sorted list hi reverse hogi

new_list = numbers.copy()
print(new_list)
# reversed list hi copy hokar new list m jaegi

















