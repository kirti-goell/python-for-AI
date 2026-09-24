#  LOOPS : to repeat code multiple times
# Python follows 0 based indexing
#  There are 2 types of loop:
# for loop : Used when you want to go through something repeatedly.
# while loop : Used when you want to keep repeating while a condition is true.

# Basic structure of FOR LOOP
# for variable in something:
#     code

for i in range(5):
    print(i)

# 0 1 2 3 4
# range(5) means Start from 0 and go up to, but NOT including, 5.

# now, we can also tell the range to python where we want to start and end
for i in range(2,7):
    print(i)

# 2 3 4 5 6

# lets perform some calculations
for i in range(2 , 8):
    print(i * 6)

# 12 18 24 30 36 42


for i in range(5):
    print("python")

# it will print python 5 times


# loop through a list

numbers = [100 , 50 , -1 , -6 , 10.8]
for num in numbers:
    print(num)

# it will print all the numbers

#  loop through a string

word = "python"
for i in word:
    print(i)

# p y t h o n

# lets loop through tuple

nums = (10, 20 , 30, 90 , 6)
for n in nums:
    print(n)
# it will print all the nums


# range() with 3 values
# range(start , stop , step) 

for i in range(3,25,3):
    print(i)
# 3 6 9 12 15 18 21 24


# this method is good for even/odd nos
for i in range(2, 11, 2):
    print(i)

# 2 4 6 8 10

# step can also be -ve
for i in range(5, 0, -1):
    print(i)
# 5 4 3 2 1


# Indentation : most imp topic of python
# for i in range(5):
#     print(i)
# print(i) has spaces before it, called indentation
# Python uses indentation to understand which code belongs to the loop.

for i in range(5, 0, -1):
    print("Number :")
    print(i)


# Conditions + loops
for i in range(1 ,6):
    if(i % 2 == 0):
        print(i)
# 2 4






#  WHILE LOOP
i = 1
while i<=5:
    print(i)
    i += 1

#  1 2 3 4 5

# Why i = i + 1 is important?
# bcs if we do not write i = i+1 then the value of i will never increase , it will remain 1 only and 1 <=5 , codn is true 
# so it will always print 1 and enter the infinite loop

# Therefore, with a while loop, you usually need to make sure something eventually makes the condition false.


# NESTED LOOP
for i in range(3):
    for j in range(2):
        print(i , j)


# break() : Immediately stop the loop.
for i in range(10):
    if(i == 5):
        break
    print(i)
# 0 1 2 3 4


# continue() : Skip this iteration and go to the next one.
for i in range(10):
    if(i == 5):
        continue
    print(i)

# 0 1 2 3 4 6 7 8 9

