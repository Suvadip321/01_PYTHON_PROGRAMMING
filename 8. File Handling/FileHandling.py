import os

# 1. Check if file exists
if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File not found")

# 2. Writing / Appending
with open("file.txt", "w") as f:      # overwrite
    f.write("Hello World\nPython is fun\n")
with open("file.txt", "a") as f:      # append
    f.write("Appended line\n")

# 3. Reading
with open("file.txt", "r") as f:
    content = f.read()               # full content
    print(content)

with open("file.txt", "r") as f:
    line = f.readline().strip()      # first line
    print(line)

with open("file.txt", "r") as f:
    lines = f.readlines()            # list of all lines
    print(lines)

# 4. Iterating line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# 5. Deleting a file (cleanup)
if os.path.exists("file.txt"):
    os.remove("file.txt")
    print("file.txt deleted")

# 6. Safe read with exception handling
try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist!")
