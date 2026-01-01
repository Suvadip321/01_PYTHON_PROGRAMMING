# =========================================
# SET CREATION
# =========================================

# Empty set (use set(), {} creates a dict)
s1 = set()
# Set with elements
s2 = {1, 2, 3, 4, 5}
# Set with mixed data types
s3 = {1, "Python", 3.14, True}
# Duplicate elements are automatically removed
s4 = {1, 2, 2, 3, 3, 3}

print("Empty set:", s1)
print("Integer set:", s2)
print("Mixed set:", s3)
print("Set with duplicates removed:", s4)

# =========================================
# SET LENGTH
# =========================================

print("\nLength of s2:", len(s2))

# =========================================
# SET OPERATIONS
# =========================================

a = {1, 2, 3}
b = {3, 4, 5}

print("\nUnion (a | b):", a | b)             # {1, 2, 3, 4, 5}
print("Intersection (a & b):", a & b)       # {3}
print("Difference (a - b):", a - b)        # {1, 2}
print("Symmetric Difference (a ^ b):", a ^ b)  # {1, 2, 4, 5}

# Membership
print("2 in a:", 2 in a)    # True
print("5 not in a:", 5 not in a)  # True

# =========================================
# SET MUTABILITY
# =========================================

s = {1, 2, 3}
s.add(4)       # Add single element
s.update({5, 6})  # Add multiple elements
print("\nAfter add and update:", s)

s.remove(2)    # Remove element (error if not found)
s.discard(10)  # Remove element (no error if not found)
print("After remove and discard:", s)

popped = s.pop()  # Remove arbitrary element
print("After pop:", s, "| Popped element:", popped)

s.clear()      # Remove all elements
print("After clear:", s)

# =========================================
# SET METHODS
# =========================================

s = {1, 2, 3, 4, 5}

print("\nOriginal set:", s)
print("Copy:", s.copy())
print("Is disjoint with {6,7}?:", s.isdisjoint({6, 7}))  # True
print("Is subset of {1,2,3,4,5,6}?:", s.issubset({1,2,3,4,5,6}))  # True
print("Is superset of {1,2}?:", s.issuperset({1,2}))       # True

# =========================================
# IMMUTABLE SET (FROZENSET)
# =========================================

fs = frozenset([1, 2, 3])
print("\nFrozen set:", fs)
# fs.add(4)  # ❌ Error, cannot modify frozen set

