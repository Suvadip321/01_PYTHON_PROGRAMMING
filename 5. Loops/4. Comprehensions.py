# Comprehensions in Python
# List, Set, Dict comprehensions + Generator (Tuple-like)

"""
Syntax:
    - List: [expr for item in iterable if condition]
    - Set:  {expr for item in iterable if condition}
    - Dict: {key: value for item in iterable if condition}
    - Generator (tuple-like): (expr for item in iterable if condition)
"""

# LIST COMPREHENSIONS
print("LIST COMPREHENSIONS:")

numbers = [x for x in range(1, 6)]               # Basic list
print("Numbers:", numbers)                       # [1, 2, 3, 4, 5]

squares = [x**2 for x in range(1, 6)]            # Squares of numbers
print("Squares:", squares)                       # [1, 4, 9, 16, 25]

evens = [x for x in range(1, 11) if x % 2 == 0]  # Condition: even numbers
print("Evens:", evens)                           # [0, 2, 4, 6, 8]


# SET COMPREHENSIONS
print("\nSET COMPREHENSIONS:")

letters = {ch for ch in "hello world" if ch.isalpha()}   # Unique letters
print("Letters:", letters)


# DICTIONARY COMPREHENSIONS
print("\n---- DICT COMPREHENSIONS ----")

word = "programming"
freq = {ch: word.count(ch) for ch in set(word) if ch.isalpha()}   # Character frequency
print("Char Frequency:", freq)                  


# GENERATOR EXPRESSIONS
print("\nGENERATOR (Tuple-like)")

gen = (x**2 for x in range(5))
print(gen)

# Convert generator to tuple
tuple_comp = tuple(x**3 for x in range(1, 6))
print("Tuple from Generator:", tuple_comp)
