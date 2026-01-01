def cal(x, y, o):
  try:
    if o == "+":
      return x + y
    elif o == "-":
      return x - y
    elif o == "*":
      return x * y
    elif o == "/":
      return x / y
    elif o == "%":
      return x % y
    elif o == "//":
      return x // y
    elif o == "**":
      return x ** y
    else:
      return "Error: Invalid operator."
  except ZeroDivisionError:
    return "Error: Division by zero not allowed."

print(cal(4, 5, "+"))
print(cal(10, 0, "/"))
