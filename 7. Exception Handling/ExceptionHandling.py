# ---------- Exception Handling Example ----------

def divide_numbers(a, b):
  try:
    # Manually raise exception if numbers are negative
    if a < 0 or b < 0:
        raise ValueError("Negative numbers not allowed")  # raise example

    # Division operation
    result = a / b

  # Specific exceptions
  except ZeroDivisionError as e:
    print("Error: Cannot divide by zero!", e)
    result = None

  except TypeError as e:
    print("Error: Invalid data type!", e)
    result = None

  except ValueError as e:
    print("Error:", e)
    result = None

  # Catch-all for any other exception
  except Exception as e:
    print("Some unexpected error occurred:", e)
    result = None

  # Executes if no exception occurs
  else:
    print("Division successful, result is:", result)

  # Executes no matter what
  finally:
    print("Execution complete.\n")

  return result

# ---------- Testing ----------
divide_numbers(10, 2)     # Valid input
divide_numbers(10, 0)     # Division by zero
divide_numbers(10, "2")   # Invalid type
divide_numbers(-5, 2)     # Negative number triggers raise
divide_numbers(None, 2)   # Unexpected error
