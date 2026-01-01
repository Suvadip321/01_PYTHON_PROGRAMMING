# Lambda functions are anonymous (no name) functions defined using the 'lambda' keyword.
# They are typically used for short, simple functions that are used only once or inline.

# 1. Basic lambda function
# -----------------------
# Syntax: lambda arguments: expression
square = lambda x: x**2  # takes x and returns x squared
print("Square of 5:", square(5))  # Output: 25

# 2. Lambda with multiple arguments
# ---------------------------------
add = lambda a, b: a + b  # takes a, b and returns their sum
print("Sum of 3 and 7:", add(3, 7))  # Output: 10

# 3. Lambda with no arguments
# ---------------------------
hello = lambda: "Hello, World!"  # no input, returns a string
print(hello())  # Output: Hello, World!

# 4. Using lambda with sorted()
# -----------------------------
# We can use lambda as a key function to sort based on custom criteria
numbers = [5, 2, 9, 1, 7]
sorted_nums = sorted(numbers, key=lambda x: x % 10)  # sorts by last digit
print("Sorted by last digit:", sorted_nums)  # Output: [1, 2, 5, 7, 9]

# 5. Using lambda with map()
# --------------------------
# map() applies a function to every element of a list
nums = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x**2, nums))  # square each number
print("Squares:", squares)  # Output: [1, 4, 9, 16, 25, 36]

# 6. Using lambda with filter()
# -----------------------------
# filter() keeps elements that satisfy a condition
evens = list(filter(lambda x: x % 2 == 0, nums))  # keep only even numbers
print("Even numbers:", evens)  # Output: [2, 4, 6]

# 7. Using lambda with reduce()
# -----------------------------
# reduce() aggregates a list into a single value using a binary function
from functools import reduce
product = reduce(lambda x, y: x * y, nums)  # multiply all numbers together
print("Product of all numbers:", product)  # Output: 720

# 8. Lambda inside another function
# ---------------------------------
# Lambda can be returned from another function for dynamic behavior
def power(n):
    return lambda x: x**n  # returns a lambda that raises x to the power of n

cube = power(3)  # lambda x: x**3
print("Cube of 4:", cube(4))  # Output: 64
