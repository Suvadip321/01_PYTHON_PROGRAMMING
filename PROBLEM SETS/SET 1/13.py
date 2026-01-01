def primes(end, start = 2):
  l = []
  for i in range(start, end+1):
    for j in range(2, i):
      if i % j == 0:
        break
    else:
      l.append(i)
  return l

print(primes(50, 20))