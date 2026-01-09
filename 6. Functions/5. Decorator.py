"""
A decorator is simply a function that takes another function as input,
adds extra functionality, and returns it.
"""

def my_decorator(func):
    def wrapper(a, b):
        print("first number:", a)
        print("second number:", b)
        print("sum:", func(a, b))
    return wrapper

@my_decorator
def add(a, b):
    return a+b

add(5, 7)
