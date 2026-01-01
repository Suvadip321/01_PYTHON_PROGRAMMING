def summation(end, start=1):
  sum = 0
  for i in range(start, end+1):
    sum += i
  return sum

print(summation(10))
print(summation(20, 10))