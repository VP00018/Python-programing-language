# Static Method = A method which belongs to class rather than any object from the class (instance) Usually used for 
# general utility functions.

# Instance Method = Best for operation on instances of the class (Object)


class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    

employee1 = Employee("Varad", "Manager")
employee2 = Employee("Yugank", "Cashier")
employee3 = Employee("Bhavesh", "Cook")

print (Employee.is_valid_position("Cook"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())



