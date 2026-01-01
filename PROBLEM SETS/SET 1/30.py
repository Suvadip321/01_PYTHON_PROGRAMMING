def cubes(end,start=1):
  d = {i: i**3 for i in range(start, end+1)}
  return d

c = cubes(10)
print(c)