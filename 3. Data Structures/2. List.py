# =========================================
# LIST CREATION
# =========================================

# Empty list
lst1 = []
# List with elements
lst2 = [1, 2, 3, 4, 5]
# List with mixed data types
lst3 = [1, "Python", 3.14, True]
# Nested list
lst4 = [[1, 2], [3, 4]]

print("Empty list:", lst1)
print("Integer list:", lst2)
print("Mixed list:", lst3)
print("Nested list:", lst4)

# =========================================
# LIST LENGTH
# =========================================

length = len(lst2)  # len() returns number of elements
print("\nLength of lst2:", length)

# =========================================
# LIST INDEXING AND SLICING
# =========================================

text_list = ["Python", "is", "awesome"]

# Indexing: Access individual elements
print("\nIndexing:")
print("text_list[0]:", text_list[0])     # First element
print("text_list[-1]:", text_list[-1])   # Last element

# Slicing: Extract sublists
print("\nSlicing:")
print("text_list[0:2]:", text_list[0:2])   # First two elements
print("text_list[:2]:", text_list[:2])     # First two elements
print("text_list[1:]:", text_list[1:])     # From second element to end
print("text_list[::-1]:", text_list[::-1]) # Reversed list

# =========================================
# LIST MUTABILITY
# =========================================

lst = [10, 20, 30]
lst[0] = 100   # ✅ Lists are mutable
print("\nModified list:", lst)

# =========================================
# LIST OPERATIONS
# =========================================

a = [1, 2, 3]
b = [4, 5, 6]

print("\nConcatenation:", a + b)  # Combine lists
print("Repetition:", a * 3)       # Repeat list

# =========================================
# COMMON LIST METHODS
# =========================================

lst = [3, 1, 4, 1, 5, 9]
print("\nOriginal list:", lst)

# Adding elements
lst.append(2)            # Add at end
lst.insert(1, 8)         # Add at index 1
lst.extend([10, 12, 16]) # Add multiple elements at the end
print("After append, insert and extend:", lst)

# Removing elements
lst.remove(1)            # Remove first occurrence of 1
popped = lst.pop()       # Remove last element and return it
print("After remove and pop:", lst, "| Popped element:", popped)

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

# =========================================
# NESTED LIST ACCESS
# =========================================

nested = [[1, 2], [3, 4], [5, 6]]
print("\nNested list element [1][0]:", nested[1][0])  # 3