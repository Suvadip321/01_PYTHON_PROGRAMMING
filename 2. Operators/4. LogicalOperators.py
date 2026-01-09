# LOGICAL OPERATORS

# AND
"""
True only if BOTH conditions are True
"""
print("AND Operator:")
print(True and True)    # True (both are True)
print(True and False)   # False (one is False)
print(False and False)  # False (both are False)

x, y = 10, 20
print((x > 5) and (y > 15))   # True and True -> True
print((x > 15) and (y > 15))  # False and True -> False
print()

# OR
"""
True if AT LEAST ONE condition is True
"""
print("OR Operator:")
print(True or True)     # True (both True)
print(True or False)    # True (one True)
print(False or False)   # False (none True)

print((x > 5) or (y < 15))    # True or False -> True
print((x < 5) or (y < 15))    # False or False -> False
print()

# NOT
"""Reverses the Boolean value"""
print("NOT Operator:")
print(not True)   # False
print(not False)  # True

print(not(x > 5))    # x=10, (10 > 5) is True -> not True = False
print(not(y < 15))   # y=20, (20 < 15) is False -> not False = True
print()

# Combining AND, OR, NOT
print("Combining Operators:")
z = 5
print((x > 5 and y > 15) or (z < 0))   
# True and True -> True, OR False -> True
print(not(x < y and z > 0))  
# (10 < 20 and 5 > 0) = (True and True) = True -> not True = False
print()

# Truthy & Falsy values with Logical Operators
"""
In Python, non-boolean values can also be used with logical operators.
Falsy values: 0, 0.0, '', [], {}, None
Truthy values: all others
"""

print("Truthy & Falsy Behavior:")
print(0 and 1)        # 0 (first falsy value returned)
print(1 and 0)        # 0 (last falsy value returned)
print(5 and 10)       # 10 (all truthy, last returned)
print(0 or 1)         # 1 (first truthy value returned)
print(1 or 0)         # 1 (first truthy value returned)
print(not "")         # True (empty string is falsy -> not falsy = True)
