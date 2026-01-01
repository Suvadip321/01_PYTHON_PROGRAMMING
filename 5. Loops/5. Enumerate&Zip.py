# ----------- ENUMERATE -----------
fruits = ["apple", "banana", "cherry"]

print("Enumerate with default start (0):")
# enumerate() returns index + value (default index starts at 0)
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

print("\nEnumerate with custom start (1):")
# You can change the starting index using the 'start' parameter
for idx, fruit in enumerate(fruits, start=1):
    print(idx, fruit)


# ----------- ZIP -----------
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print("\nUsing zip() to combine lists:")
# zip() pairs elements from two or more iterables (like lists, tuples)
# Here, it pairs each name with its corresponding score
for name, score in zip(names, scores):
    print(name, score)

# Important: zip() stops when the shortest iterable is exhausted
grades = ["A", "B"]  # Notice this list is shorter
print("\nZipping 3 lists (stops at shortest):")
for name, score, grade in zip(names, scores, grades):
    print(name, score, grade)

# zip() objects can also be converted to a list of tuples
print("\nList of tuples from zip():")
print(list(zip(names, scores)))
