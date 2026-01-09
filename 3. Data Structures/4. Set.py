# SET CREATION
# Empty set (use set(), {} creates a dict)
s1 = set()
# Set with elements
s2 = {1, 2, 3, 4, 5}
# Set with mixed data types
s3 = {1, "Python", 3.14, True}
# Duplicate elements are automatically removed
s4 = {1, 2, 2, 3, 3, 3}

print(s1)
print(s2)
print(s3)
print(s4)


# SET OPERATIONS
a = {1, 2, 3}
b = {3, 4, 5}

print("\nUnion (a | b):", a.union(b))                              # {1, 2, 3, 4, 5}
print("Intersection (a & b):", a.intersection(b))                  # {3}
print("Difference (a - b):", a.difference(b))                      # {1, 2}
print("Symmetric Difference (a ^ b):", a.symmetric_difference(b))  # {1, 2, 4, 5}


# SET MUTABILITY
s = {1, 2, 3}

s.add(4)          # Add single element
s.update({5, 6})  # Add multiple elements
print("\nAfter add and update:", s)

s.remove(2)    # Remove element (error if not found)
s.discard(10)  # Remove element (no error if not found)
print("After remove and discard:", s)

popped = s.pop()  # Remove arbitrary element
print("After pop:", s)

s.clear()      # Remove all elements
print("After clear:", s)


# SET METHODS
s = {1, 2, 3, 4}

print("\nOriginal set:", s)
print("Length:", len(s))
print("Copy:", s.copy())
print("Is disjoint with {6,7}?:", s.isdisjoint({6, 7}))           # True
print("Is subset of {1,2,3,4,5,6}?:", s.issubset({1,2,3,4,5,6}))  # True
print("Is superset of {1,2}?:", s.issuperset({1,2}))              # True

# FROZEN SET (IMMUTABLE)
frozen = frozenset([1, 2, 3])
print(f"\nfrozen set: {frozen}")
