# LIST CREATION
# Empty list
l1 = []
# List with same data type
l2 = [1, 2, 3, 4, 5]
# List with mixed data types
l3 = [3, "Python", 3.14, True]
# Nested list
l4 = [[1, 2], [3, 4]]

print(l1)
print(l2)
print(l3)
print(l4)


# LENGTH, INDEXING & SLICING
l = ["p", "y", "t", "h", "o", "n"]

# len() -> returns number of elements in a list
print("\nLength:", len(l))

# Indexing: Access individual elements
print("\nIndexing:")
print(l[0])    # First element 'p'
print(l[-1])   # Last element 'n'
list_2d = [[1, 2], [3, 4], [5, 6]]
print(list_2d[0][1])

# Slicing: Extract a sublist [start:end:step]
print("\nSlicing:")
print(l[0:6:1])
print(l[0:4]) 
print(l[:3])
print(l[2:])
print(l[:])
print(l[::2])
print(l[::-1])


# LIST MUTABILITY 
lst = [10, 20, 30]
lst[0] = 100
print("\nModified list:", lst)


# LIST OPERATIONS
a = [1, 2, 3]
b = [4, 5, 6]

print("\nConcatenation:", a + b)  # Combine lists
print("Repetition:", a * 3)       # Repeat list


# COMMON LIST METHODS
lst = [3, 1, 4, 1, 5, 9]
print("\nOriginal list:", lst)

# Adding elements
lst.append(2)             # Add at end
lst.insert(1, 8)          # Add at index 1
lst.extend([10, 12, 16])  # Add multiple elements at the end
print("After append, insert and extend:", lst)

# Removing elements
lst.remove(1)   # Remove first occurrence of 1
lst.pop()       # Remove last element and return it
lst.pop(0)      # Remove at index
print("After remove and pop:", lst)

# Sorting and reversing
lst.sort()               # Sort list in ascending order
print("Sorted list:", lst)
lst.reverse()            # Reverse list
print("Reversed list:", lst)

# Counting and index
print("Count of 1:", lst.count(1))
print("Index of 5:", lst.index(5))

# Copying and clearing
lst_copy = lst.copy()    # Shallow copy
lst.clear()              # Clear original list
print("Copied list:", lst_copy, "| Cleared list:", lst)
