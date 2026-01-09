# Inheritance allows a class (child class) to inherit properties and behaviors (attributes and methods) from another class (parent class)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_role(self):
        return "Person"
    def introduce(self):
        return f"Hi, I am {self.name}, my age is {self.age}, and I am a {self.get_role()}"

class Student(Person):
    def __init__(self, name, age, stream):
        super().__init__(name, age)
        self.stream = stream
    
    def get_role(self):
        return "Student"
    
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def get_role(self):
        return "Teacher"

p1 = Student("Alice", 20, "CSE")
print(p1.introduce())
print(p1.stream)

p2 = Teacher("Bob", 35, "DSA")
print(p2.introduce())
print(p2.subject)
