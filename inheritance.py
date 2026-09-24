# Inheritance : it lets you create new class based on existing ones.the newclass(child) gets everything 
# from the parent class , plus it can adds its own stuff

# parent class
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        return f"{self.name} is eating"
    def sleep(self):
        return f"{self.name} is sleeping"


# child class
class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof"


dog1 = Dog("bunny")
dog2 = Dog(name = "fasty")

print(dog1.eat())
print(dog1.bark())

animal = Animal("frootzy")
animal.eat()
animal.sleep()
# its wrong bcs parent class can not inherit prop of child class
animal.bark()
