def countDigits(n):
  n = abs(n)
  return len(str(n))

n = int(input("Enter an integer: "))
print(countDigits(n))