def swap(a, b):
  a, b = b, a
  return a, b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = swap(a, b)
print(f"\nAfter swapping:\nFirst number = {a}\nSecond number = {b}")