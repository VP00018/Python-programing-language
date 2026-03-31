# Class Variable = shared amoung all instances of class 
#                  Defined outside the Constructor 
#                  Allow you to share data among all objects created from that class

class Student:

    class_year = 2029
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Varad", 18)
student2 = Student("Yugank", 19)
student3 = Student("Bhavesh", 20)
student4 = Student("Tanay", 17)

print(f"My Graduation class of {Student.class_year} has {Student.num_students} students")

print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)