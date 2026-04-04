# Duck = Another way to Achieve ploymorphism besides inheritance object must have the minimum necessary attributes./
# EX :- IF IT LOOK LIKE A DUCK AND QUACKS LIKE DUCK, IT MUST BE A DUCK.

class Animal:
    alive = True

class Dog(Animal):
    def speak (self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Car:

    alive = True

    def speak(self):
        print("HONK!!!!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)