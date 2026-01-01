# Polymorphism allows the same interface or method name to behave differently depending on the object or context

# Method Overriding
class Animal:
  def sound(self):
    print("Animal makes a sound.")

class Dog(Animal):
  def sound(self):
    print("Dog barks.")
    
Animal().sound()
Dog().sound()

# Duck Typing
class Human:
  def talk(self):
    print("Hello!")
    
class Duck:
  def talk(self):
    print("Quack")
    
Human().talk()
Duck().talk()