# Inheritance = Allow a class to inherit attributes and methods from another class. 

class Animal:
    
    def __init__ (self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("Meowwww!")

class Mouse(Animal):
     def speak(self):
        print("SQUEEK!")

dog = Dog("Tommy")
cat = Cat("kitti")
mouse = Mouse("Mikki")

dog.speak()