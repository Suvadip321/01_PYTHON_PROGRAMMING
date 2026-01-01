l = []
n = int(input("Enter size of the list: "))
for i in range(1, n+1):
  l.append(int(input(f"Enter element {i}: ")))
  
print(f"Your list is: {l}")
es = 0
os = 0
sum = 0
for el in l:
  sum += el
  if el % 2 == 0:
    es += el
  else:
    os += el
print(f"Total sum of numbers in the list = {sum}")
print(f"sum of even numbers in the list = {es}")
print(f"sum of odd numbers in the list = {os}")