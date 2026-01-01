# =======================================
# Comprehensions in Python
# =======================================
# List, Set, Dict comprehensions + Generator (Tuple-like)
#
# Syntax:
#   - List: [expr for item in iterable if condition]
#   - Set:  {expr for item in iterable if condition}
#   - Dict: {key: value for item in iterable if condition}
#   - Generator (tuple-like): (expr for item in iterable if condition)
# =======================================


# -----------------------------
# 1. LIST COMPREHENSIONS
# -----------------------------
print("---- LIST COMPREHENSIONS ----")

numbers = [x for x in range(5)]             # Basic list
print("Numbers:", numbers)                  # [0, 1, 2, 3, 4]

squares = [x**2 for x in range(6)]          # Squares of numbers
print("Squares:", squares)                  # [0, 1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]  # Condition: even numbers
print("Evens:", evens)                      # [0, 2, 4, 6, 8]


# -----------------------------
# 2. SET COMPREHENSIONS
# -----------------------------
print("\n---- SET COMPREHENSIONS ----")

squares_set = {x**2 for x in range(6)}      # Unique values only
print("Squares Set:", squares_set)          # {0, 1, 4, 9, 16, 25}

letters = {ch for ch in "hello world" if ch.isalpha()}  # Unique letters
print("Letters:", letters)                  # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}


# -----------------------------
# 3. DICTIONARY COMPREHENSIONS
# -----------------------------
print("\n---- DICT COMPREHENSIONS ----")

squares_dict = {x: x**2 for x in range(6)}  # {number: square}
print("Squares Dict:", squares_dict)        

evens_dict = {x: x**2 for x in range(10) if x % 2 == 0}  # Only evens
print("Evens Dict:", evens_dict)            

word = "programming"
freq = {ch: word.count(ch) for ch in set(word)}  # Character frequency
print("Char Frequency:", freq)                  


# -----------------------------
# 4. GENERATOR EXPRESSIONS (Tuple-like)
# -----------------------------
print("\n---- GENERATOR (Tuple-like) ----")

# Looks like tuple comprehension, but it's a generator
gen = (x**2 for x in range(5))
print("Generator Object:", gen)             # <generator object ...>
print("Type:", type(gen))                   # <class 'generator'>

# Convert generator to tuple
tuple_comp = tuple(x**2 for x in range(5))
print("Tuple from Generator:", tuple_comp)  # (0, 1, 4, 9, 16)
