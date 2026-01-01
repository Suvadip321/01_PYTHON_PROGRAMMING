# Class Attributes: Shared by all objects
# Instance Attributes: Belong to each object
# Methods: Functions inside a class

class Student:
  college = "SKFGI"     # Class attribute
  
  def __init__(self, name, age, gpa):     # Instance attributes
    self.name = name
    self.gpa = gpa
    self.age = age
    
  def details(self):     # Instance method
    return f"Name: {self.name}, Age: {self.age}, GPA: {self.gpa}, College: {Student.college}"
  
  print("Here is the details of the students:")
  

s1 = Student("Suvadip Kushari", "20", "9.00")
s2 = Student("Sounak Chatterjee", "20", "8.50")

print(f"Student1: {s1.details()}")
print(f"Student2: {s2.details()}")