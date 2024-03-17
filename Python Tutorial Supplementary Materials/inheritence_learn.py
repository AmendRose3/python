class Animal:
    def breath(self):
        print("Breathing")

class Cat(Animal):  # Inherited from Animal
    def meow(self):
        print("Meowwwww!!!!!!")

class Dog(Animal):  # Inherited from Animal
    def bark(self):
        print("Bowwwww!!!!!!")

# Creating instances
d1 = Dog()
c1 = Cat()

# Calling methods
d1.breath()
d1.bark()

c1.breath()
c1.meow()
