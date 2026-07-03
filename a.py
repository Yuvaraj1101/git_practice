# Parent Class
class Animal:

    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


# Child Class 1
class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed      # Encapsulation

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

    # Polymorphism
    def sound(self):
        print(self.name, "says Woof Woof")


# Child Class 2
class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    # Polymorphism
    def sound(self):
        print(self.name, "says Meow")


# Objects
dog = Dog("Rocky", "Labrador")
cat = Cat("Kitty")

dog.sound()
cat.sound()

print("Breed:", dog.get_breed())

dog.set_breed("Golden Retriever")

print("Updated Breed:", dog.get_breed())