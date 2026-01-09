"""
break → exits the loop immediately
continue → skips the current iteration
pass → does nothing (used as a placeholder)
"""

# Example 1: Normal loop (no break, continue, or pass)
print("Example 1 (no break, continue, pass):")
for i in range(10):
    print(i, end=" ")
print("\n")

# Example 2: Using break (stops loop when i == 6)
print("Example 2 (with break):")
for i in range(10):
    if i == 6:
        break
    print(i, end=" ")
print("\n")

# Example 3: Using continue (skips i == 6)
print("Example 3 (with continue):")
for i in range(10):
    if i == 6:
        continue
    print(i, end=" ")
print("\n")

# Example 4: Using pass (does nothing, loop continues normally)
print("Example 4 (with pass):")
for i in range(10):
    if i == 6:
        pass  # placeholder for future logic
    print(i, end=" ")
print("\n")
