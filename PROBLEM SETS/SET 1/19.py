# def sod(n):
#   sum = 0
#   while n > 0:
#     sum += n % 10
#     n //= 10
#   return sum

def sod(n):
  n = str(n)
  sum = 0
  for i in n:
    sum += int(i)
  return sum

n = int(input("Enter an integer: "))
print(sod(n))

