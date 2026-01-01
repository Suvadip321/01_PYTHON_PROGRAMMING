# =========================================
# DICTIONARY CREATION
# =========================================

# Empty dictionary
dict1 = {}

# Dictionary with key-value pairs
dict2 = {"name": "Alice", "age": 25, "city": "New York"}

# Dictionary with mixed keys
dict3 = {1: "one", "two": 2, 3.0: "three"}

# Nested dictionary
dict4 = {
    "person1": {"name": "Bob", "age": 30},
    "person2": {"name": "Carol", "age": 27}
}

print("Empty dictionary:", dict1)
print("Dictionary with key-value pairs:", dict2)
print("Dictionary with mixed keys:", dict3)
print("Nested dictionary:", dict4)

# =========================================
# DICTIONARY LENGTH
# =========================================

print("\nLength of dict2:", len(dict2))

# =========================================
# ACCESSING ELEMENTS
# =========================================

print("\nAccessing elements:")
print("Name:", dict2["name"])                    # Direct key access
print("Age:", dict2.get("age"))                  # Using get()
print("Country:", dict2.get("country", "Not Found"))  # Default if key missing

# =========================================
# DICTIONARY MUTABILITY
# =========================================

dict2["country"] = "USA"     # Add new key-value pair
dict2["age"] = 26            # Update existing key
print("\nAfter adding/updating:", dict2)

# Deleting elements
del dict2["city"]            # Delete by key
popped_val = dict2.pop("country")  # Remove and return value
print("After deletions:", dict2, "| Popped value:", popped_val)

# =========================================
# DICTIONARY METHODS
# =========================================

sample = {"a": 1, "b": 2, "c": 3}

print("\nOriginal dictionary:", sample)
print("Keys:", sample.keys())     # dict_keys(['a', 'b', 'c'])
print("Values:", sample.values()) # dict_values([1, 2, 3])
print("Items:", sample.items())   # dict_items([('a', 1), ('b', 2), ('c', 3)])

copy_dict = sample.copy()        # Copy dictionary
sample.clear()                   # Clear dictionary
print("Copied dictionary:", copy_dict)
print("Cleared dictionary:", sample)

# =========================================
# NESTED DICTIONARY ACCESS
# =========================================

nested_dict = {
    "person1": {"name": "Bob", "age": 30},
    "person2": {"name": "Carol", "age": 27}
}

print("\nNested dictionary access:")
print("Person1's name:", nested_dict["person1"]["name"])
print("Person2's age:", nested_dict["person2"]["age"])

# =========================================
# ADDITIONAL USEFUL OPERATIONS
# =========================================

# Merge two dictionaries
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 3, "z": 4}
merged_dict = dict_a | dict_b
print("\nMerged dictionary (dict_a | dict_b):", merged_dict)

# Update dictionary with another
dict_a.update(dict_b)
print("Updated dict_a with dict_b:", dict_a)
