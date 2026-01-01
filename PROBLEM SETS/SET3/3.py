def div(a, b):
  try:
    return a / b
  except ZeroDivisionError:
    print("Cannot divide by zero!")
    return None
  
print(div(20, 10))
print(div(20, 0))