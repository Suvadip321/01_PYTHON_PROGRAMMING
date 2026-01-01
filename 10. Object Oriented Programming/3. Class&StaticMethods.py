class maths:
  pi = 3.141     # class attribute
  
  def __init__(self, radius):
    self.radius = radius     # instance attribute
    
  # Instance method (works on object data)
  def area(self):
    return maths.pi * self.radius * self.radius
  
  # Class method (works on class level data)
  @classmethod
  def circleArea(cls, r):
    return cls.pi * r * r
  
  # Static method (utility function, independent of class/object)
  @staticmethod
  def add(a, b):
    return a + b
  
  

circle = maths(7)
print(f"Instance method: {circle.area()}")

print(f"Class method: {maths.circleArea(7)}")

print(f"Static method: {maths.add(2, 3)}")