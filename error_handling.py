# Their are diff types of error that can happen
# 1. syntax error
# x is not defined , colon is missing
# if x >5
#   print("its greater than 5")



# 2. Runtime error : you wont see the error until you run it
x = 10/0

# print(score) score is not defined
# print("hello" + 5) type error bcs str can not be concated with int

# but we can do
5+5
"hello" + "hiii"

# and much more types of error


# so, try and except means agar koi is type ka error hai to ye kro m smbhal lungi
# their should be atleast one except or finally block with try
# syntax
# try:
#     condn that ca cause an error
# except:
    #   that runs when the error happens

try:
    x = 10/0
except:
    print("hi there")


try:
    age = int(input("Enter your age : "))
    print(f"In 10 years your age will be : {age + 10}")
except ValueError:
    print("pls enter a number")

# their are other erros too like FileNotFoundError , ZeroDivisionError
# we can also add else block , finally block(finally block always executes)

try:
    x = 10/0
except:
    print("hi there")
finally:
    print("i am a winner")