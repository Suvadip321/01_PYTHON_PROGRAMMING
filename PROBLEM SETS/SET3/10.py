def divide_numbers(a, b):
  try:
    result = a / b
    
  except ZeroDivisionError as e:
    print("Error: Cannot divide by zero!", e)
    result = None

  except TypeError as e:
    print("Error: Invalid data type!", e)
    result = None

  except ValueError as e:
    print("Error:", e)
    result = None
    
  except Exception as e:
    print("Some unexpected error occurred:", e)
    result = None
    
  else:
    print("Division successful, result is:", result)

  finally:
    print("Execution complete.\n")

  return result

divide_numbers(10, 2)    
divide_numbers(10, 0)     
divide_numbers(10, "2")       
divide_numbers(None, 2)   