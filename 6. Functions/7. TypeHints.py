# Type hints are added using colon (:) syntax for variables and the -> syntax for function return types.

# Variable type hints
age: int = 20

# Function type hints
def greet(name: str) -> str:
  return f"Hello, {name}!"

print(greet("Alice"))

# Python's typing module provides more advanced type hints such as List, Tuple, Dict, and Union
from typing import List, Tuple, Dict, Union

# List of integers
nums: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"