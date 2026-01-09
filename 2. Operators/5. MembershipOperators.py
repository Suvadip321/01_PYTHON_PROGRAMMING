# MEMBERSHIP OPERATORS (in, not in)

# In STRING
text = "Python Programming"
print('P' in text)          # True
print('z' in text)          # False
print('Pro' in text)        # True
print('thon' not in text)   # False


# In LIST / TUPLE
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)        # True
print("mango" in fruits)        # False
print("banana" not in fruits)   # False

numbers = (1, 2, 3, 4, 5)
print(3 in numbers)       # True
print(10 not in numbers)  # True


# In SET
colors = {"red", "green", "blue"}
print("red" in colors)          # True
print("yellow" not in colors)   # True


# In DICTIONARY (checks only KEYS, not values)
person = {"name": "Alice", "age": 25, "city": "Delhi"}
print("name" in person)     # True (key check)
print("Alice" in person)    # False (values not checked)
print("age" not in person)  # False


# Combine with conditional logic
if "banana" in fruits:
    print("Banana is in the fruit list!")

if "mango" not in fruits:
    print("Mango is not in the fruit list!")
