def binary(dec):
  bin = ""
  while dec > 0:
    rem = dec % 2
    bin = str(rem) + bin
    dec //= 2
  return bin if bin != "" else "0"


n = int(input("Enter a decimal number: "))
print(f"Binary of {n} is {binary(n)}")