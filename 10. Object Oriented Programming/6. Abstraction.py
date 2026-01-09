# Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecessary details
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        return "Vehicle must start"
    
    @abstractmethod
    def stop(self):
        return "Vehicle must stop"
    
class Bike(Vehicle):
    def start(self):
        return "Bike starts"
    def stop(self):
        return "Bike stops"

bike = Bike()

class Car(Vehicle):
    def start(self):
        pass

# car = Car() # this will throw error, because to be a vehicle it must have start and stop function
