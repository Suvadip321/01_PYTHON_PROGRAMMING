def fact(n):
  if n < 0:
    return 
  f = 1
  for i in range(1, n + 1):
    f *= i
  return f

n = int(input("Enter a number: "))
print(f"{n}! = {fact(n)}")