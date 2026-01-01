# Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecessary details

from abc import ABC, abstractmethod

class abstract(ABC):
  @abstractmethod
  def area(self):
    pass
  
class Circle(abstract):
  def __init__(self, radius):
    self.radius = radius
    
  def area(self):
    return 3.14 * self.radius * self.radius

obj = Circle(7)
