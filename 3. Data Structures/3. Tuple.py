# =========================================
# TUPLE CREATION
# =========================================

# Empty tuple
t1 = ()
# Tuple with elements
t2 = (1, 2, 3, 4)
# Tuple with mixed data types
t3 = (1, "Python", 3.14, True)
# Nested tuple
t4 = (1, (2, 3), 4)

print("Empty tuple:", t1)
print("Integer tuple:", t2)
print("Mixed tuple:", t3)
print("Nested tuple:", t4)

# =========================================
# TUPLE LENGTH
# =========================================

length = len(t2)
print("\nLength of t2:", length)

# =========================================
# TUPLE INDEXING AND SLICING
# =========================================

text_tuple = ("Python", "is", "awesome")

# Indexing
print("\nIndexing:")
print("text_tuple[0]:", text_tuple[0])    # First element
print("text_tuple[-1]:", text_tuple[-1])  # Last element

# Slicing
print("\nSlicing:")
print("text_tuple[0:2]:", text_tuple[0:2])   # First two elements
print("text_tuple[:2]:", text_tuple[:2])     # First two elements
print("text_tuple[1:]:", text_tuple[1:])     # From second element to end
print("text_tuple[::-1]:", text_tuple[::-1]) # Reversed tuple

# =========================================
# TUPLE IMMUTABILITY
# =========================================

t = (10, 20, 30)
# t[0] = 100  # ❌ Error, tuples are immutable
new_t = (100,) + t[1:]  # ✅ Create a new tuple
print("\nOriginal tuple:", t)
print("Modified tuple (new tuple):", new_t)

# =========================================
# TUPLE OPERATIONS
# =========================================

a = (1, 2, 3)
b = (4, 5, 6)

print("\nConcatenation:", a + b)  # Combine tuples
print("Repetition:", a * 3)       # Repeat tuple

# =========================================
# TUPLE METHODS
# =========================================

t = (3, 1, 4, 1, 5, 9)

print("\nOriginal tuple:", t)

# Counting occurrences
print("Count of 1:", t.count(1))
# Index of first occurrence
print("Index of 4:", t.index(4))

# =========================================
# TUPLE UNPACKING
# =========================================

# Basic unpacking
t = (10, 20, 30)
a, b, c = t
print("\nTuple:", t)
print("Unpacked values:", a, b, c)

# Nested tuple unpacking
nested = (1, (2, 3), 4)
x, (y, z), w = nested
print("\nNested tuple:", nested)
print("Unpacked values:", x, y, z, w)

# Using * for variable-length unpacking
t2 = (1, 2, 3, 4, 5)
first, *middle, last = t2
print("\nTuple with * unpacking:", t2)
print("First:", first)
print("Middle:", middle)
print("Last:", last)

# Swapping values using tuple unpacking
x, y = 5, 10
print("\nBefore swap: x =", x, ", y =", y)
x, y = y, x
print("After swap: x =", x, ", y =", y)