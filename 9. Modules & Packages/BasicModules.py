# ================================
# 1. os - File and directory operations
# ================================
import os

# print(os.getcwd())                  # Current working directory
# print(os.listdir())                 # List files/folders in current dir
# os.makedirs("data/folder", exist_ok=True)  # Create directories
# os.rename("old.txt", "new.txt")    # Rename file
# os.remove("file.txt")              # Delete file
# print(os.path.exists("file.txt"))  # Check existence
# print(os.path.join("folder", "file.txt"))  # Join paths

# ================================
# 2. math - Mathematical functions
# ================================
import math

print(math.sqrt(16))       # Square root
print(math.pow(2, 3))      # Power: 2^3
print(math.ceil(2.3))      # Ceiling
print(math.floor(2.7))     # Floor
print(math.factorial(5))   # Factorial
print(math.gcd(12, 18))    # Greatest common divisor
print(math.pi, math.e)     # Constants

# ================================
# 3. random - Random numbers
# ================================
import random

print(random.random())             # Random float 0.0 - 1.0
print(random.randint(1, 10))      # Random integer 1-10
print(random.choice([1,2,3,4]))   # Random element from list
print(random.choices([1,2,3,4], k=2))  # Random multiple elements
l = [1, 2, 3, 4]
random.shuffle(l)      # Shuffle list in-place
print(l) 
print(random.uniform(1, 5))       # Random float 1.0 - 5.0
