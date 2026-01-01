# --- MEMBERSHIP OPERATORS ---

# In STRING
text = "Python Programming"
print("'P' in text:", 'P' in text)          # True
print("'z' in text:", 'z' in text)          # False
print("'Pro' in text:", 'Pro' in text)      # True
print("'thon' not in text:", 'thon' not in text)  # False


# In LIST
fruits = ["apple", "banana", "cherry"]
print("'apple' in fruits:", "apple" in fruits)   # True
print("'mango' in fruits:", "mango" in fruits)   # False
print("'banana' not in fruits:", "banana" not in fruits) # False


# In TUPLE
numbers = (1, 2, 3, 4, 5)
print("3 in numbers:", 3 in numbers)       # True
print("10 not in numbers:", 10 not in numbers)  # True


# In SET
colors = {"red", "green", "blue"}
print("'red' in colors:", "red" in colors)   # True
print("'yellow' not in colors:", "yellow" not in colors) # True


# In DICTIONARY (checks only KEYS, not values)
person = {"name": "Alice", "age": 25, "city": "Delhi"}
print("'name' in person:", "name" in person)     # True (key check)
print("'Alice' in person:", "Alice" in person)   # False (values not checked)
print("'age' not in person:", "age" not in person) # False


# Combine with conditional logic
if "banana" in fruits:
    print("Banana is in the fruit list!")   # Will print

if "mango" not in fruits:
    print("Mango is not in the fruit list!") # Will print


