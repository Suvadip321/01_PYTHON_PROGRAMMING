def CtoF(c):
  f = (c * (9 / 5)) + 32
  return f
  
c = float(input("Enter temperature in C: "))
print(f"Temperature in F: {CtoF(c)}")