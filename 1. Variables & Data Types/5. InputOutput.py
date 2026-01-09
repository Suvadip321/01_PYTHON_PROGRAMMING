# OUTPUT (print)
"""
We use print() to display values on the screen
"""
print("Hello, World!")  
# Output: Hello, World!


# INPUT (input)
"""
input() is used to take input from the user as a string
"""
name = input("Enter your name: ")
print("Hello,", name)
# Example Input: Suvadip
# Output: Hello, Suvadip


# TYPE CONVERSION FOR INPUT
"""
By default, input() returns a string. 
We need to convert it to int, float, etc. if needed.
"""
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1, "years old.")
# Example Input: 20
# Output: Next year, you will be 21 years old.

# FORMATTED OUTPUT
"""Using f-strings for clean and formatted printing"""
marks = 95
print(f"Your marks are {marks}/100")
# Output: Your marks are 95/100
