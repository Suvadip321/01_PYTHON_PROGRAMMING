# -------------------------------
# Commonly Used Basic Built-in Functions in Python
# -------------------------------

# 1. Output and Input
print("1) Output and Input")
print("Hello, World!")             # Prints output
name = input("Enter your name: ")  # Takes input as string
print("You entered:", name)
print("-" * 40)

# 2. Type Checking and Conversion
print("2) Type Checking and Conversion")
x = "100"
print("Type of x:", type(x))       # <class 'str'>
y = int(x)                         # str -> int
z = float(x)                       # str -> float
print("Converted:", y, z, type(y), type(z))
print("-" * 40)

# 3. Length and Absolute
print("3) Length and Absolute")
print(len("Python"))       # 6 (length of string)
print(len([1, 2, 3, 4]))   # 4 (length of list)
print(abs(-25))            # 25 (absolute value)
print("-" * 40)

# 4. Min, Max, Sum
print("4) Min, Max, Sum")
numbers = [5, 10, 2, 8]
print("Min:", min(numbers))   # 2
print("Max:", max(numbers))   # 10
print("Sum:", sum(numbers))   # 25
print("-" * 40)

# 5. Rounding and Power
print("5) Rounding and Power")
print(round(3.14159))          # 3
print(round(3.14159, 2))       # 3.14 (rounded to 2 decimals)
print(pow(2, 3))               # 8 (2^3)
print("-" * 40)

# 6. Sorting
print("6) Sorting")
nums = [4, 1, 7, 3]
print("Ascending:", sorted(nums))              # [1, 3, 4, 7]
print("Descending:", sorted(nums, reverse=True)) # [7, 4, 3, 1]
print("-" * 40)

# 7. Type Casting Helpers
print("7) Type Casting Helpers")
print(str(123))       # "123"
print(int("456"))     # 456
print(float("3.14"))  # 3.14
print(list("abc"))    # ['a', 'b', 'c']
print("-" * 40)

# 8. Checking Conditions
print("8) Checking Conditions")
print(all([True, True, 1]))    # True (all elements True)
print(all([True, False, 1]))   # False
print(any([False, 0, ""]))     # False (all falsy)
print(any([False, 0, "Hi"]))   # True (since "Hi" is True)
print("-" * 40)

# 9. Range (with for loop)
print("9) Range (with for loop)")
for i in range(3):
    print(i, end=" ")   # 0 1 2
print("\n" + "-" * 40)

# 10. Reversed
print("10) Reversed")
nums = [1, 2, 3, 4]
for val in reversed(nums):
    print(val, end=" ")   # 4 3 2 1
print("\n" + "-" * 40)
