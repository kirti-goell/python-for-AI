# oops : it is a way of writing code so that related data and 
# functions can be grouped together

# classes : class is a blueprint to create object.it defines
# attributes : what an object can have
# methods : what an object can do

# without oops : tools scattered everywhere
# with oops : tools placed on their named compartments

# __init__ double underscores method is called a dunder method
# self refers to the curr object , its how obj can keep the track of its data

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("jerry barks")
# attributes = name,breed

class Cat:
    def __init__(self, name,color):
        self.name = name
        self.color = color

jerry = Dog(name="jerry" , breed="labrador")
jerry.name
jerry.breed
jerry.bark()
# whatever we have learned in functions , is applicable in methods
# below will give error
dog = Dog(name="tim")

# we can also give def values to the methods like fun
class Dog:
    def __init__(self,name,breed="None"):
        self.name = name
        self.breed = breed

dog = Dog(name="tim")
dog.breed
# none



# Real world example
class APIConfig:
    def __init__(self , api_key , model = "gpt-3.5-turbo" , max_tokens = 100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# object is instance of class
dev_config = APIConfig("sk-dev-config" , max_tokens = 50)
prod_config = APIConfig("sk-prod-key",model = "gpt-4" , max_tokens = 1000)

print(dev_config.model)
print(prod_config.model)
print(prod_config.max_tokens)
print(prod_config.api_key)
print(prod_config.base_url)


# class with attributes and methods
class DataValidator:
    def __init__(self):
        self.errors = []

    def validateEmail(self,email):
        if '@' not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True

    def validateAge(self , age):
        if(age < 0 or age > 150):
            self.errors.append(f"Invalid age: {age}")
            return False
        return True

    def getErrors(self):
        return self.errors
    
validator = DataValidator()

validator.validateEmail(email="incorrect email")
validator.validateAge(age = 10)

validator.validateAge(200)
validator.validateEmail("valid@")

print(validator.getErrors())




