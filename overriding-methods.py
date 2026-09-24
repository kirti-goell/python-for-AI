class Animal:
    def __init__(self,name):
        self.name = name

    def make_sounds(self):
        return f"{self.name} makes sound"

class Dog(Animal):
    def make_sounds(self):
        return f"{self.name} makes sound: woof"

class Cat(Animal):
    def make_sounds(self):
        return f"{self.name} makes sound: meowww"

animal = Animal("squeezy")
animal.make_sounds()

dog = Dog("lemo")
dog.make_sounds()

cat = Cat("ricco")
cat.make_sounds()