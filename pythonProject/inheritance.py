#Parent class/Superclass/Base class
class Animal:
    def sound(self):
        print("Animal is speaking")
#Child class/Sub class/Derived class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Cat(Animal):
    def meow(self):
        print("A cat meows")
a = Animal()
b = Dog()
b.sound()
