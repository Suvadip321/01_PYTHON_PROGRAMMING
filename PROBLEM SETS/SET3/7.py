def evens(n):
  for i in range(0, n+1, 2):
    yield i
    
for even in evens(10):
  print(even)