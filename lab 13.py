# Step 1: Define the Person class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I live at {self.address}.")

# Step 2: Define the Student class that inherits from Person
class Student(Person):
    def __init__(self, name, age, address, student_id, major):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.major = major
    
    def study(self):
        print(f"{self.name} is studying {self.major}.")
    
    def introduce(self):
        super().introduce()
        print(f"I am a student majoring in {self.major} with student ID {self.student_id}.")

# Step 3: Define the Teacher class that inherits from Person
class Teacher(Person):
    def __init__(self, name, age, address, employee_id, subject):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subject = subject
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")
    
    def introduce(self):
        super().introduce()
        print(f"I am a teacher with employee ID {self.employee_id}, and I teach {self.subject}.")

# Step 4: Create objects of Student and Teacher classes
# Creating a Student object
student = Student(name="Alice", age=20, address="123 Maple Street", student_id="S1001", major="Computer Science")
student.introduce()
student.study()

# Creating a Teacher object
teacher = Teacher(name="Mr. Smith", age=40, address="456 Oak Avenue", employee_id="T2001", subject="Mathematics")
teacher.introduce()
teacher.teach()