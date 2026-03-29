# object = A bundle of related Attributes (Variables) and methods (Functions)
# EX = phone,cup,book
# you need to "class" TO create many object 

class Car:
    def __init__ (self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

car1 = Car("AUDI", 2024, "RED", False)

print(car1.model)
print(car1.year)
