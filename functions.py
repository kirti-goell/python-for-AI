# Functions : create reusable block of code
# build in functions like : print() , len()


# Defining function : create your own reusable code
#  a fun is a named block that performs specific task. it is created once and can be called multiple times when ever needed

def greet():
    print("hello duniya")
    print("lets learn python")
    pass
# pass is a readable way for humans and it simply means this fun does not return anything
# pass is our choice , iske likhe bina bhi code valid hai
print("mei fun k bhar hu")
greet(); 


# Naming funs : 1. always use lowercase letters
# 2. between 2 words use underscores only
# 3. be descriptive about what it does
#  example : their is a function which calculates gross product 
# so the name should be gross_product
# def Calculate(): , it will not give error but it looks like that you re a begineer


# Calling function

def greet():
    print("hello duniya")
    print("lets learn python")
    

print("mei fun k bhar hu")
greet(); 
greet(); 
greet(); 



def check_weather():
    temp = 25
    if(temp >= 20):
        print("its hot")
    else:
        print("its normal")

check_weather()


# parameters : pass data into your function
# innstead of hardcoding data into functions , we make inputs flexible

def greet_kirti():
    print("hello, kirti")
greet_kirti()

# now , make it dynamic

def greet(name):
    print(f"hello, {name}" )
greet("Kirti")
greet(name = "dhruv")


def full_name(first_name , last_name):
    print(f"i'm {first_name} {last_name}")

# positional arguments : order matters
full_name("kirti" , "goel")
# keyword arguments : order does not matter
full_name(last_name="goel" , first_name="kirti")


# functions can have default parameters too : alwways keep parameter first with non default values else it eill give error
def full_name( last_name,first_name = "kirti"):
    print(f"i'm {first_name} {last_name}")

full_name(last_name="goel")
full_name(first_name="dhruv" , last_name= "goel")


# local vs global scope of vars
def calculator(price , tax , discount):
    tax = price * tax
    final_price = price + tax - discount 
    print (f"Final amount is : ${final_price}")

# print(f"discount : {discount}")
calculator(1000 , 5 , 3)
# print(f"discount : {discount}")

#  for the above code it will give error bcs discount is not defined
#  discount has only local scope inside the function only

discount = 45
def calculator(price , tax , discount):
    tax = price * tax
    final_price = price + tax - discount 
    print (f"Final amount is : ${final_price}")

print(f"discount : {discount}")
calculator(1000 , 5 , 3)

# here , discount will be printed as it have global scope
# notice one thing : global dis ko change krengy tb bhi final amnt chnage ni hoga bcs vo priortise krega local dis ko




# Returning values : getting results back from function
# as of now we have printed the output . But sometimes we requires a value from function so that we can use it else where
def add_print(a,b):
    print(a+b)
ans= add_print(10,5)
ans
# here ans is empty 

def add_return(a,b):
    return a+b
res = add_return(10,5)
res
# 15
# interactive mode me return wala bhi print krta hai but not on terminal



def double(number):
    return number*2

# store in var
result = double(5)

# use in expression
total = double(5) + double(3)

# Pass to other functions
print(double(10))

# use in condns
if(double(7)>10):
    print("its a big number")



# a fun can also return multiple values
def simple_fun():
    numbers = [1,2,3,4,5]
    first = numbers[0]
    last = numbers[-1]
    return first, last

# answers = simple_fun()
# answers 
# (1,5)

f,l = simple_fun()
f
l

# 1
# 5