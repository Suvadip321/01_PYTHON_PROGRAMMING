# =========================================
# STRING CREATION
# =========================================

# Single quotes
s1 = 'Hello'
# Double quotes
s2 = "World"
# Triple quotes (multi-line strings)
s3 = '''Python 
supports
multi-line strings'''
# Empty string
s4 = "" 

print("s1:", s1)
print("s2:", s2)
print("s3:\n", s3)
print("s4 (Empty string):", s4)

# =========================================
# STRING LENGTH
# =========================================

s = "Suvadip"
length = len(s)  # len() returns the number of characters in a string
print(f"\nLength of '{s}' is {length}")

# =========================================
# STRING INDEXING AND SLICING
# =========================================

text = "Python"

# Indexing: Access individual characters
print("\nIndexing:")
print("text[0]:", text[0])    # First character 'P'
print("text[-1]:", text[-1])  # Last character 'n'

# Slicing: Extract a substring [start:end:step]
print("\nSlicing:")
print("text[0:4]:", text[0:4])      # 'Pyth' (from index 0 to 3)
print("text[:3]:", text[:3])        # 'Pyt' (from start to 2)
print("text[2:]:", text[2:])        # 'thon' (from index 2 to end)
print("text[:]:", text[:])          # 'Python' (full string)
print("text[::2]:", text[::2])      # 'Pto' (every 2nd character)
print("text[::-1]:", text[::-1])    # 'nohtyP' (reversed string)

# =========================================
# STRING IMMUTABILITY
# =========================================

word = "Hello"
# word[0] = "J"  # ❌ Cannot change string directly
new_word = "J" + word[1:]  # ✅ Correct way: create a new string
print("\nImmutability Example:", new_word)

# =========================================
# STRING OPERATIONS
# =========================================

a = "Python"
b = "Programming"

print("\nConcatenation:", a + " " + b)  # Join strings
print("Repetition:", a * 3)             # Repeat string 3 times

# =========================================
# COMMON STRING METHODS
# =========================================

s = "  Python Programming is Fun  "
print("\nOriginal string (with spaces):", s)

# Case conversion
print("capitalize():", s.capitalize())  # Capitalize first letter of string
print("lower():", s.lower())            # Convert all characters to lowercase
print("upper():", s.upper())            # Convert all characters to uppercase
print("title():", s.title())            # Capitalize first letter of each word

# Remove leading/trailing spaces
print("strip():", s.strip())            # Remove spaces from both ends

# Searching and counting
print("find('Prog'):", s.find("Prog"))  # Index of substring
print("count('m'):", s.count('m'))      # Count occurrences of 'm'
print("startswith('Python'):", s.startswith("Python"))  # Check if string starts with 'Python'
print("endswith('Fun'):", s.endswith("Fun"))            # Check if string ends with 'Fun'

# Replacing substring
print("replace('Fun', 'Awesome'):", s.replace("Fun", "Awesome"))

# Splitting and Joining
words = s.split()                         # Split string into list of words
print("split():", words)
joined = "-".join(words)                  # Join list into string with delimiter '-'
print("join():", joined)

# =========================================
# STRING CHECK METHODS
# =========================================

check_str = "Python3"

print("\nisalpha():", check_str.isalpha())   # False, contains a number
print("isdigit():", check_str.isdigit())     # False, contains letters
print("isalnum():", check_str.isalnum())     # True, letters+numbers
print("islower():", check_str.islower())     # False, not all lowercase
print("isupper():", check_str.isupper())     # False, not all uppercase
