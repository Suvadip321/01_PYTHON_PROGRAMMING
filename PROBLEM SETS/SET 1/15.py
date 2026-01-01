def fib(n):
  a = 0
  b = 1
  l = []
  for i in range(1, n+1):
    l.append(a)
    c = a + b
    a = b
    b = c
  return l

print(fib(10))