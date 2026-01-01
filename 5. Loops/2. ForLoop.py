# -------------------------------
# for loop with range()
# -------------------------------

# range(stop) → 0 to stop-1
for i in range(5):
    print(i, end=" ")
print("\n")

# range(start, stop) → start to stop-1
for i in range(1, 5):
    print(i, end=" ")
print("\n")

# range(start, stop, step) → skips by step
for i in range(1, 10, 2):
    print(i, end=" ")
print("\n")

# Decreasing loop using negative step
for i in range(10, 1, -2):
    print(i, end=" ")
print("\n\n")


# -------------------------------
# Iterating with for loop over different data types
# -------------------------------

# String
print("Iterating over a string:")
name = "Python"
for ch in name:
    print(ch)
print()

# List
print("Iterating over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print()

# Tuple
print("Iterating over a tuple:")
numbers = (2, 4, 6, 8)
for num in numbers:
    print(num)
print()

# Set
print("Iterating over a set:")
unique_nums = {10, 20, 30, 40}
for val in unique_nums:
    print(val)
print()

# Dictionary (keys)
print("Iterating over a dictionary (keys):")
student = {"name": "Suvadip", "age": 20, "grade": "A"}
for key in student:
    print(key)
print()

# Dictionary (keys and values)
print("Iterating over a dictionary (keys and values):")
for key, value in student.items():
    print(key, "->", value)
print("\n")


# -------------------------------
# for loop with else
# -------------------------------

# Case 1: Normal completion (else runs)
print("for-else example (no break):")
for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop finished without break!")
print()

# Case 2: Break encountered (else skipped)
print("for-else example (with break):")
for i in range(5):
    if i == 3:
        print("\nBreaking at", i)
        break
    print(i, end=" ")
else:
    print("This won't print because loop was broken!")
print("\n")


# -------------------------------
# Nested for loops
# -------------------------------

# Example: Pattern printing
print("Right-angled triangle pattern:")
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
