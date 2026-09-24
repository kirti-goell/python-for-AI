# Operator : It is a symbol/ keyword that tells python to perform some operations
# Types of operator

# 1. Arithmetic operators : = , - , * , / , % , // (floor division) , ** (power)

a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
# floor division means remove decimals and round down towards negative infinity
print(a//b)
print(a**b)

# -7  // 2 => -3.5 => -4 (floor val of -3.5 is -4)


# 2. Comparison operators : == , != , > , >= , < , <=
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)


# 3. Assignment operators : = , += , -= , *= , /=
a = 10
a += 10
a -= 10
a /= 10
a *= 10


# 4. Logical operators : and , or , not
age = 20
print (age > 18 and age < 25)
print (age > 18 or age < 25)
print(not age > 18) 
#  age > 18 = true and bcs of not its false


# 5. Membership operators : in , not in 
# they are used to check whether something exists inside a sequence like a string / list

name = "python"
print("z" not in name)
print("z" in name)

numbers = [1,2,3,4,5] 
print(5 in numbers)

# Sequence of operators : BODMAS
n = (1 + 99 * 500 / 5) - 33
print(n)

i = (1 + 2 * 3)
print(i)
# 7

i = (1 + 2 * 3) * 9
print(i)
#  63

