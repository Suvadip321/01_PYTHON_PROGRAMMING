# VARIABLES
"""
A variable is a name that stores a value in memory.
Python is dynamically typed -> no need to declare type explicitly.
"""

x = 10            # integer
y = 3.14          # float
name = "Python"   # string
is_active = True  # boolean

print(x, y, name, is_active)
# Output: 10 3.14 Python True


# REASSIGNING VARIABLES
"""
Variables can be reassigned with new values (even of a different type).
"""
x = 50
print("x =", x)  
# Output: x = 50

x = "Now This is a string!"
print("x =", x)  
# Output: x = Now This is a string!


# MULTIPLE ASSIGNMENT
"""Assigning multiple values to multiple variables in one line"""
a, b, c = 1, 2, 3
print(a, b, c)  
# Output: 1 2 3

"""Assigning the same value to multiple variables"""
p = q = r = 0
print(p, q, r)  
# Output: 0 0 0


# VARIABLE NAMING RULES
"""
Cannot start with a number
Can contain letters, numbers, underscores
Case-sensitive (age, Age, AGE are all different)
Keywords (like for, if, while) cannot be used as variable names
"""
