"""
Lambda functions are anonymous (no name) functions defined using the 'lambda' keyword.
They are typically used for short, simple functions that are used only once or inline
"""
greet = lambda: "Hello, this is lambda function!"
print(greet())

sqrt = lambda x: x**0.5
print(sqrt(9))

add = lambda a, b: a + b
print(add(3, 7))


# Using lambda with map()
"""map() applies a function to every element of a list"""
nums = [1, 2, 3, 4, 5, 6, 7]
squares = list(map(lambda x: x**2, nums))
print(squares)


# Using lambda with filter()
"""filter() keeps elements that satisfy a condition"""
nums = [1, 2, 3, 4, 5, 6, 7]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)


# Using lambda with reduce()
"""reduce() aggregates a list into a single value using a binary function"""
from functools import reduce
nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)
