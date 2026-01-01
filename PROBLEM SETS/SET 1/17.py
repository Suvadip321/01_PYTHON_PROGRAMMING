def lcm(a, b):
  m = a if a > b else b
  for i in range(m, a*b + 1):
    if i % a == 0 and i % b == 0:
      return i

print(lcm(12, 15))