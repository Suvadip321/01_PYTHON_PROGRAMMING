def gcd(a, b):
  m = a if a < b else b
  for i in range(1, m+1):
    if a % i == 0 and b % i == 0:
      x = i
  return x

print(gcd(12, 20))