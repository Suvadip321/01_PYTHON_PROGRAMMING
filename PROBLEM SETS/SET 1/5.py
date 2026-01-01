def MaxOfThree(a, b, c):
  if a > b and a > c:
    max = a
  elif b > a and b > c:
    max = b
  else:
    max = c
  return max

print(MaxOfThree(11, 23, 17))
  