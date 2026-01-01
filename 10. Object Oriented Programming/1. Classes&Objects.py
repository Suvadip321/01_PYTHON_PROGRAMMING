# Class: A blueprint for creating objects
# Object (Instance): A real entity created from a class

# Defining a class
class Car:
  def __init__(self, brand, model):     # constructor
    self.brand = brand
    self.model = model
    
  def show(self):                       # method
    return f"{self.brand} {self.model}"
  
# creating objects (instances)
car1 = Car("Tesla", "Model 5")
car2 = Car("BMW", "X5")

print(f"Car1 details: {car1.show()}")
print(f"Car2 details: {car2.show()}")

# Key points:
# __init__ : Constructor (runs when object is created)
# self : refers to the current object