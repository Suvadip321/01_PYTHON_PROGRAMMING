# --- OUTPUT (print) ---
# We use print() to display values on the screen
print("Hello, World!")  
# Output: Hello, World!


# --- INPUT (input) ---
# input() is used to take input from the user as a string
name = input("Enter your name: ")  # User types something
print("Hello,", name)
# Example Input: Subhadip
# Output: Hello, Subhadip


# --- TYPE CONVERSION FOR INPUT ---
# By default, input() returns a string. 
# We need to convert it to int, float, etc. if needed.
age = int(input("Enter your age: "))  # Convert input to integer
print("Next year, you will be", age + 1, "years old.")
# Example Input: 20
# Output: Next year, you will be 21 years old.


# --- TAKING MULTIPLE INPUTS ---
# We can take multiple inputs in one line using split()
a, b = input("Enter two numbers separated by space: ").split()
print("a =", a, "| b =", b)
# Example Input: 5 10
# Output: a = 5 | b = 10

# Converting them into integers
a, b = map(int, input("Enter two numbers: ").split())
print("Sum =", a + b)
# Example Input: 5 10
# Output: Sum = 15


# --- FORMATTED OUTPUT ---
# Using f-strings for clean and formatted printing
marks = 95
print(f"Your marks are {marks}/100")
# Output: Your marks are 95/100
