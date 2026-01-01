# -------------------------------
# Basic while loop
# -------------------------------
print("Basic while loop (print 1 to 10):")
i = 1
while i <= 10:
    print(i)       # Print current value of i
    i += 1         # Increment i to avoid infinite loop

print("\n")

# -------------------------------
# Nested while loops
# -------------------------------
print("Nested while loops:")
i = 1
while i <= 2:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

print("\n")

# -------------------------------
# Infinite while loop with break
# -------------------------------
print("Infinite while loop with break:")
i = 1
while True:         # Infinite loop
    print(i)
    if i == 3:
        break       # Exit loop when i equals 3
    i += 1

print("\n")

# -------------------------------
# Using continue to skip iteration
# -------------------------------
print("Using continue to skip 3:")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue   # Skip current iteration
    print(i)

print("\n")


# -------------------------------
# Using pass in while loop
# -------------------------------
print("Using pass in while loop:")
i = 1
while i <= 5:
    if i == 3:
        pass        # Placeholder, does nothing
    print(i)
    i += 1

print("\n")

# -------------------------------
# While loop with user input
# -------------------------------
print("While loop with user input (Enter 5 to exit):")
num = 0
while num != 5:
    num = int(input("Enter a number: "))
    print("You entered:", num)
print("Exited loop")

print("\n")