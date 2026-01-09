# STRING CREATION
s1 = 'Hello'
s2 = "World"
s3 = '''
Python supports
multi-line strings
'''
s4 = "" 

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s4 (Empty string):", s4)


# LENGTH, INDEXING & SLICING
s = "Python"

# len() -> returns number of characters in a string
print("\nLength:", len(s))

# Indexing: Access individual characters
print("\nIndexing:")
print(s[0])    # First character 'P'
print(s[-1])   # Last character 'n'

# Slicing: Extract a substring [start:end:step]
print("\nSlicing:")
print(s[0:6:1])     # 'Python (full string)'
print(s[0:4])       # 'Pyth' (from index 0 to 3)
print(s[:3])        # 'Pyt' (from start to 2)
print(s[2:])        # 'thon' (from index 2 to end)
print(s[:])         # 'Python' (full string)
print(s[::2])       # 'Pto' (every 2nd character)
print(s[::-1])      # 'nohtyP' (reversed string)


# STRING IMMUTABILITY
print("\nImmutability:")
word = "Hello"
# word[0] = "J"             # Cannot change string directly
new_word = "J" + word[1:]   # Correct way: create a new string
print(word, new_word)


# STRING OPERATIONS
a = "Python"
b = "Programming"

print("\nConcatenation:", a + " " + b)     # Join strings
print("Repetition:", a * 3)                # Repeat string 3 times


# COMMON STRING METHODS
s = "python programming is fun!"
print("\nOriginal string:", s)

# conversion
print("capitalize():", s.capitalize())  # Capitalize first letter of string
print("lower():", s.lower())            # Convert all characters to lowercase
print("upper():", s.upper())            # Convert all characters to uppercase
print("title():", s.title())            # Capitalize first letter of each word
print("strip():", s.strip())            # Remove spaces from both ends

# Searching and counting
print("find('prog'):", s.find("prog"))                  # Index of substring
print("count('m'):", s.count('m'))                      # Count occurrences of 'm'
print("startswith('python'):", s.startswith("python"))  # Check if string starts with 'Python'
print("endswith('fun!'):", s.endswith("fun!"))            # Check if string ends with 'Fun'

# Replacing substring
print("replace('fun', 'awesome'):", s.replace("fun", "awesome"))

# Splitting and Joining
words = s.split()                         # Split string into list of words
print("split():", words)
joined = "-".join(words)                  # Join list into string with delimiter '-'
print("join():", joined)

# Checking
check_str = "Python3"

print("\nisalpha():", check_str.isalpha())   # False, contains a number
print("isdigit():", check_str.isdigit())     # False, contains letters
print("isalnum():", check_str.isalnum())     # True, letters+numbers
print("islower():", check_str.islower())     # False, not all lowercase
print("isupper():", check_str.isupper())     # False, not all uppercase
