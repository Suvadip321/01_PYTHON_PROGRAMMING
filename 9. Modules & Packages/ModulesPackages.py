# ------------------ MODULES ------------------
# A module is simply a Python file containing functions, classes, or variables.

# file: math_utils.py   (this is a module)
# file: strings.py

# ------------------ PACKAGES ------------------
# A package is a collection of modules organized in directories with an __init__.py file.

# Folder structure:
# Modules & Packages/
# ├── __init__.py
# ├── math_utils.py
# └── string_utils.py

# ------------------ USING MODULES & PACKAGES ------------------
from maths import add, mul             # importing module functions
from strings import to_upper, to_lower              

print("Addition:", add(2, 3))        
print("Multiplication:", mul(4, 5)) 
print("Upper:", to_upper("python")) 
print("Upper:", to_lower("PYTHON"))


# ------------------ IMPORTANT NOTE ------------------
# The line below is used to make sure that some code runs only when the file is executed directly, not when imported as a module.

if __name__ == "__main__":
    print("This runs only when this file is executed directly")
