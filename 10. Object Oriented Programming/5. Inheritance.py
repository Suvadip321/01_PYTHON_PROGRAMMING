# Inheritance allows a class (child class) to inherit properties and behaviors (attributes and methods) from another class (parent class)

# Single Inheritance
class Animal:
  def __init__(self, name):
    self.name = name
  
  def sound(self):
    return f"{self.name} makes a sound."
  
class Dog(Animal):
  def speak(self):
    return f"{self.name} barks."

dog = Dog("Ranit")
print(dog.sound())
print(dog.speak())

# Multilevel Inheritance
class Mammal(Animal):
  def feed(self):
    return f"{self.name} feeds milk."
  
class Cat(Mammal): # Cat inherits from Mammal, which inherits from Animal
  def speak(self):
    return f"{self.name} meows."
  
cat = Cat("Buddha")
print(cat.speak())
print(cat.feed())

# Multiple Inheritance
class Flyer:
  def fly(self):
    return f"{self.name} can fly."

class Bird(Flyer, Animal):
  def speak(self):
    return f"{self.name} chirps!"
  
bird = Bird("Sanju")
print(bird.fly())
print(bird.speak())

# Super() method: used to access the methods of a super class in the derived class
class Human(Animal):
  def __init__(self, name, age):
    super().__init__(name)
    self.age = age
    
  def speak(self):
    return f"Hello, I am {self.name}, my age is {self.age}"
  
person = Human("Suvadip",20)
print(person.speak())
