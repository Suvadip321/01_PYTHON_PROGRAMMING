# Commonly Used Basic Built-in Functions in Python

# 1. Output and Input
print("1) Output and Input")

name = input("Enter your name: ")
print(f"Welcome, {name}!")

print("-" * 40)

# 2. Type Checking and Conversion
print("2) Type Checking and Conversion")

x = "100"
print(x, type(x))

y = int(x)                    
z = float(x)                    
print(y, type(y))
print(z, type(z))

print("-" * 40)

# 3. Abs, Rounding, Power
print("5) Abs, Rounding and Power")

print(abs(-25))
print(round(3.14159, 2))
print(pow(2, 3)) 

print("-" * 40)

# 4. Length, Min, Max, Sum
print("4) Min, Max, Sum")

print(len("Python"))
print(len([1, 2, 3, 4]))

numbers = [5, 10, 2, 8]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print("-" * 40)

# 5. Sorting
print("6) Sorting")

nums = [4, 1, 7, 3, 5]
print("Ascending:", sorted(nums))
print("Descending:", sorted(nums, reverse=True))

print("-" * 40)

# 6. Type Casting Helpers
print("7) Type Casting Helpers")
num = 122333

String = str(num)
print(String)

List = list(String)
print(List)

Set = set(List)
print(Set)

print("-" * 40)

# 7. Checking Conditions
print("8) Checking Conditions")

print(all([True, True, True]))
print(all([True, False, True]))
print(any([False, True, False]))
print(any([False, False, False]))

print("-" * 40)
