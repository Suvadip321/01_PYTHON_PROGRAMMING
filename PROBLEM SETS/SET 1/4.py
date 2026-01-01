def mulTab(n, upto=10):
  for i in range(1, upto+1):
    print(f"{n} x {i} = {n * i}")

n = int(input("Enter a number: "))
mulTab(n)