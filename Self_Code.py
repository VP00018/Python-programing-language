class Students:
    def __init__(self):
        self.name = " "
        self.Rollno = 0
        self.Marks = 0.0
    def X_data(self):
        self.name = input("Enter the name of the student: ")
        self.Rollno = int(input("Enter the Rollno of the student: "))
        self.Marks = float(input("Enter the Marks of the student: "))
    def Display(self):
        print("Name of the student",self.name)
        print("Rollno of the student",self.Rollno)
        print("Marks of the student",self.Marks)

n = int(input("Enter the number of students: "))
Students_list = []
for i in range(n):
    print(f"Students{i+1}:")
    obj = Students()
    Students_list.append(obj)
    obj.X_data()
print("The Details of student are: ")
for s in Students_list:
    s.Display()
    