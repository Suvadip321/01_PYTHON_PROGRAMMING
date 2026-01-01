# A decorator is simply a function that takes another function as input,
# adds extra functionality, and returns it.

# Step 1: Define a decorator
def my_decorator(func):
    def wrapper(a, b):
        print("Addition to your numbers is:")   # extra functionality
        func(a, b)                                  # original function
        print("Thank you!")                     # extra functionality
    return wrapper

# Step 2: Use the decorator with @ syntax
@my_decorator
def add(a, b):
    print(a + b)

# Step 3: Call the decorated function
add(5, 7)
